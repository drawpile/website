from confusable_homoglyphs import confusables

def normalize_username(name):
    """Generate a normalized version of a username for preventing
    deceptively similar names."""

    # First step: names should be case insensitive
    name = name.lower()

    # Replace confusable characters
    # In version 3.0.0, this can fail with a TypeError if the character is not found
    #homoglyphs = confusables.is_confusable(name, greedy=True, preferred_aliases=['latin'])

    # Workaround:
    homoglyphs = []
    for c in name:
        try:
            homoglyphs += confusables.is_confusable(c, preferred_aliases=['latin'])
        except TypeError:
            pass

    if homoglyphs:
        mapping = {
            x['character']: x['homoglyphs'][0]['c']
            for x in homoglyphs
            }
        name = ''.join(mapping.get(c, c) for c in name)

    return name

