
class RfbConnectionFailed(Exception):
    """raised in case a rfb connection failed"""


class RfbClientHandshakeSecurityTypeFailed(Exception):
    """raised in case the security handshake failed"""


class RfbClientSecResultFailed(Exception):
    """raised in case the security result failed"""
