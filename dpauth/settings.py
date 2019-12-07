from django.conf import settings

def null_group_membership(username, group):
    """Default group membership test.
    Gives HOST permission to all users and MOD permission to those
    with dpauth.moderator Django permission.

    Custom implementations can delegate to this one if group is blank.

    Parameters:
    username -- the Username instance or None if this is a guest user
    group    -- group name or None if no group was specified
    """

    if group:
        return None

    flags = ['HOST']
    if username and username.is_mod and username.user.has_perm('dpauth.moderator'):
        flags.append('MOD')

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
