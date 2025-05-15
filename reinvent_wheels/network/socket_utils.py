"""Small socket/hostname helpers used to tag logs and messages with the
name of the machine that produced them.
"""
import socket


def get_safe_hostname(default: str = 'unknown-host') -> str:
    """Returns the local hostname, falling back to `default` if the lookup
    fails (e.g. in a sandboxed container without a resolvable hostname).
    """
    try:
        return socket.gethostname()
    except Exception:
        return default
