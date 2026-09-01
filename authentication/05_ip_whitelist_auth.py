# $ python3 05_ip_whitelist_auth.py
#
# Service-to-service auth for trusted internal callers: no token at all,
# just "did this request arrive from an IP/subnet we trust, carrying a
# caller-supplied identity". Only safe behind a proxy that itself
# verifies the source (a plain client-supplied header is trivial to
# spoof over the open internet) — this is for internal networks, not
# public APIs.

import ipaddress


class IPWhitelistAuthenticator:
    def __init__(self, trusted_networks):
        self.trusted_networks = [ipaddress.ip_network(n) for n in trusted_networks]

    def _is_trusted(self, ip: str) -> bool:
        addr = ipaddress.ip_address(ip)
        return any(addr in net for net in self.trusted_networks)

    def authenticate(self, source_ip: str, claimed_user_id):
        if not self._is_trusted(source_ip):
            return None
        if claimed_user_id is None:
            return None
        return {"user_id": int(claimed_user_id)}


if __name__ == "__main__":
    auth = IPWhitelistAuthenticator(trusted_networks=["10.0.0.0/8", "192.168.1.5/32"])

    print("internal caller:", auth.authenticate("10.1.2.3", claimed_user_id=42))
    print("exact-match host:", auth.authenticate("192.168.1.5", claimed_user_id=7))
    print("untrusted caller:", auth.authenticate("203.0.113.9", claimed_user_id=42))
