from typing import Union
from balderhub.rfb.lib import features
from .local_test_rfb_server_feature import LocalTestRfbServerFeature


class ProtocolInjectorFeature(features.server.ProtocolInjectorFeature):
    """
    setup feature that allows to set a protocol version for the shipped :class:`RfbServer`
    """

    server = LocalTestRfbServerFeature()

    def set_protocol_version(self, protocol_bytes: Union[bytes, bytearray]):
        self.server.set_protocol_version(protocol_bytes)
