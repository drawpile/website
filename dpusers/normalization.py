import re


_IGNORES_DOTS = set(
    [
        "gmail.com",
        "googlemail.com",
        "pm.me",
        "proton.me",
        "protonmail.ch",
        "protonmail.com",
    ]
)


def normalize_email(email):
    normalized = email.strip().casefold()
    if "@" in normalized:
        prefix, suffix = normalized.rsplit("@", 2)

        # We'll just assume that all email services support plus addressing.
        # If there's a conflict later, we can fix it then.
        plus_index = prefix.find("+")
        if plus_index > 0:
            prefix = prefix[0:plus_index]

        # Some email services ignore dots in the local part.
        if suffix in _IGNORES_DOTS:
            prefix = prefix.replace(".", "")

        return prefix + "@" + suffix
    else:
        return normalized
