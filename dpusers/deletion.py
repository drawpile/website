from django.db.models import Q

from dpauth.models import Username
from gallery.models import Submission, Comment, Group, GroupMembership

def get_cascade_deletion_list(user):
    """Return a list of items (relevant to the human user) that will be
    deleted when a user account is deleted.

    Returns a list:

        [
            (count, "label")
        ]
    """

    return filter(lambda x : x[0] > 0,
        [
            _usernames(user),
            _submissions(user),
            _my_comments(user),
            _other_comments(user),
            _groups(user)
        ])

def _usernames(user):
    count = Username.objects.filter(user=user).count()
    return (count, 'username' if count == 1 else 'usernames')


def _submissions(user):
    count = Submission.objects.filter(uploaded_by=user).count()
    return (count, 'gallery submission' + ('' if count == 1 else 's'))

def _my_comments(user):
    count = Comment.objects.filter(user=user).count()
    return (count, 'comment' + ('' if count == 1 else 's'))

def _other_comments(user):
    count = Comment.objects.filter(Q(submission__uploaded_by=user) & ~Q(user=user)).count()
    return (count, 'comment' + ('' if count == 1 else 's') + ' on your submissions')

def _groups(user):
    my_groups = GroupMembership.objects.filter(user=user, status__in=GroupMembership.MEMBER_STATUSES).select_related('group')
    
    groups = []
    for g in my_groups:
        if g.group.groupmembership_set.filter(status__in=GroupMembership.MEMBER_STATUSES).count() == 1:
            groups.append(g.group.title)

    return (len(groups), 'group' if len(groups)==1 else 'groups')
