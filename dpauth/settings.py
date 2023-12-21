from django.conf import settings
from . import models

def null_group_membership(username, group):
    """Default group membership test.
    Gives HOST permission to all users, MOD permission to those
    with dpauth.moderator Django permission and GHOST permission to those
    with dpauth.ghost Django permission.

    Custom implementations can delegate to this one if group is blank.

    Parameters:
    username -- the Username instance or None if this is a guest user
    group    -- group name or None if no group was specified
    """

    if group:
        return None

    flags = ['HOST']
    if username:
        if username.is_mod and username.user.has_perm('dpauth.moderator'):
            flags.append('MOD')
            if username.is_ghost and username.user.has_perm('dpauth.ghost'):
                flags.append('GHOST')
        try:
            verification = models.UserVerification.objects.get(pk=username.user_id)
            if verification.exempt_from_bans:
                flags.append('BANEXEMPT')
        except models.UserVerification.DoesNotExist:
            pass

    return {
        'member': False,
        'flags': flags,
        }


DEFAULTS = {
    'GUEST_LOGINS': True, # Support guest logins
    'ALT_COUNT': 4,       # Maximum number of usernames per account
    'PRIVATE_KEY': '',    # The login token signing key
    'PUBLIC_KEY': '',     # The login token verification key
    'GROUP_IMPL': null_group_membership,  # Group implementation
}


extauth_settings = DEFAULTS.copy()
extauth_settings.update(getattr(settings, 'DRAWPILE_EXT_AUTH', {}))
