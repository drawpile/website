from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response

from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.conf import settings

from .querysets import get_community_list_queryset
from .serializers import (
    CommunityListSerializer, CommunityDetailSerializer,
    MembershipSerializer, InviteMemberSerializer, JoinSerializer,
    AbuseReportSerializer,
)

from communities.models import Community, Membership
from communities.webhooks import send_abusereport

class ReportAbuseAnonRateThrottle(AnonRateThrottle):
    rate = "1/minute"

class ReportAbuseUserRateThrottle(UserRateThrottle):
    rate = "1/minute"

class CommunityViewSet(viewsets.ReadOnlyModelViewSet):
    REPORT_ABUSE_CACHE_KEY = "drawpile_community_report_abuse"
    lookup_field = 'slug'

    def get_queryset(self):
        return get_community_list_queryset(self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CommunityListSerializer
        elif self.action == 'members':
            return InviteMemberSerializer
        elif self.action == 'member':
            return MembershipSerializer
        elif self.action == 'join':
            return JoinSerializer
        elif self.action == 'report_abuse':
            return AbuseReportSerializer

        return CommunityDetailSerializer

    @action(
        detail=True,
        methods=("post",),
        permission_classes=(AllowAny,),
        throttle_classes=(ReportAbuseAnonRateThrottle, ReportAbuseUserRateThrottle),
    )
    def report_abuse(self, request, slug):
        url = getattr(settings, 'ADMIN_REPORT_WEBHOOK', '')
        if not url:
            return Response(
                {'error': 'Reporting not configured!'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        community = self.get_object()

        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        ok = send_abusereport(
            url,
            community,
            serializer.validated_data['comment'],
            self.request.user
        )
        
        if not ok:
            return Response(
                {'error': 'An error occurred and report delivery failed.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=('post',))
    def join(self, request, slug):
        community = self.get_object()

        try:
            existing = Membership.objects.get(
                community=community,
                user=self.request.user
            )

            if existing.status == Membership.STATUS_INVITED:
                existing.status = Membership.STATUS_MEMBER
                existing.save(update_fields=('status',))

            return Response(
                MembershipSerializer(
                    existing,
                    context=self.get_serializer_context()
                ).data,
                headers={
                    'Location': reverse(
                        'api:community-member',
                        kwargs={
                            'slug': slug,
                            'user': self.request.user.username
                        }
                    ),
                }
            )

        except Membership.DoesNotExist:
            pass

        if community.group_policy == Community.GROUP_INVITE_ONLY:
            raise Http404
        elif community.group_policy == community.GROUP_VERIFIED_JOIN:
            s = Membership.STATUS_PENDING
        else:
            s = Membership.STATUS_MEMBER

        m = Membership.objects.create(
            community=community,
            user=self.request.user,
            status=s
        )

        return Response(
            MembershipSerializer(
                m,
                show_ban=False,
                context=self.get_serializer_context()
            ).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=('get', 'post'))
    def members(self, request, slug):
        community = self.get_object()

        if request.method == 'POST':
            if not community.can_admin(self.request.user):
                raise Http404

            serializer = InviteMemberSerializer(
                data=self.request.data,
                context={'community': community}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

        else:
            if not community.can_see_memberlist(self.request.user):
                raise Http404

        serializer = MembershipSerializer(
            Membership.objects.filter(community=community).order_by('user__username'),
            show_ban=community.can_admin(self.request.user),
            many=True
        )

        return Response(serializer.data)

    @action(detail=True, url_path=r'members/(?P<user>[^/]+)', methods=('get', 'put', 'delete'))
    def member(self, request, slug, user):
        community = self.get_object()
        is_admin = community.can_admin(self.request.user)
        is_self = self.request.user.username == user
        if not (is_admin or is_self):
            raise Http404

        membership = get_object_or_404(
            Membership,
            community=community,
            user__username=user
        )

        if self.request.method == 'DELETE':
            membership.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Non-admins can only delete themselves        
        if not is_admin:
            raise Http404

        serializer = self.get_serializer(membership, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
