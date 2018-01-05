from dpauth.models import Username

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
        ])

def _usernames(user):
    count = Username.objects.filter(user=user).count()
    return (count, 'username' if count == 1 else 'usernames')

