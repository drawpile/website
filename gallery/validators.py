from django.core.exceptions import ValidationError

import re

# Regexes from https://stackoverflow.com/questions/106179/regular-expression-to-match-dns-hostname-or-ip-address
VALID_IP = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
VALID_DOMAIN = re.compile(r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$')

def hostname_validator(hostname):
    if not VALID_IP.match(hostname) and not VALID_DOMAIN.match(hostname):
        raise ValidationError("Invalid IP address or domain name")
