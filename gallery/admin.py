from django.contrib import admin
from django.db.models import Count

from . import models

class GroupMembershipAdmin(admin.TabularInline):
    model = models.GroupMembership
    extra = 1

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'approve_joins', 'user_count', 'submission_count')
    inlines = (GroupMembershipAdmin,)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            user_count=Count('groupmembership'),
            submission_count=Count('submission')
        )

    def user_count(self, obj):
        return obj.user_count
    user_count.short_description = 'Users'

    def submission_count(self, obj):
        return obj.submission_count
    submission_count.short_description = 'Submissions'


class PictureSubmissionAdmin(admin.StackedInline):
    model = models.Picture
    extra = 0

class SubmissionCommentAdmin(admin.StackedInline):
    model = models.Comment
    extra = 0

@admin.register(models.Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('uploaded_by', 'submission_type', 'title', 'is_visible')
    list_filter = ('groups',)
    search_fields = ('uploaded_by__username', 'title')
    inlines = (PictureSubmissionAdmin, SubmissionCommentAdmin)

