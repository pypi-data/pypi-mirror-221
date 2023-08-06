from typing import Union
import balder


class ProtocolInjectorFeature(balder.Feature):
    """feature that allows to set a protocol version"""

    def set_protocol_version(self, protocol_bytes: Union[bytes, bytearray]):
        """
        This method sets a protocol version that should be returned by the server

        :param protocol_bytes: the protocol that should be returned by the server
        """
        raise NotImplementedError()
