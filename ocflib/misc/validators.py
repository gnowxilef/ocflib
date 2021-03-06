"""Misc validators for things like emails, domains, etc."""
import re

import dns
import dns.resolver

from ocflib.infra.net import OCF_DNS_RESOLVER


def host_exists(host):
    try:
        message = dns.message.make_query(host, dns.rdatatype.ANY)
    except dns.name.EmptyLabel:
        return False

    response = dns.query.udp(message, str(OCF_DNS_RESOLVER))
    return bool(response.answer)


def email_host_exists(email_addr):
    """Verifies that the host of the email address exists"""
    if '@' in email_addr:
        host = email_addr.rsplit('@', 1).pop()
        return host_exists(host)
    return False


def valid_email(email):
    """Check the email with naive regex and check for the domain's MX record.
    Returns True for valid email, False for bad email."""
    regex = r'^[a-z0-9._%\-+]+@([a-z0-9._%\-]+.[a-z]{2,})$'

    m = re.match(regex, email, re.IGNORECASE)
    if m:
        domain = m.group(1)
        try:
            # Check that the domain has MX record(s)
            return bool(dns.resolver.query(domain, 'MX'))
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass
    return False
