from typing import Union, List
import balder
from balderhub.rfb.lib.features.server.rfb_server_config import RfbServerConfig
from balderhub.rfb.lib.utils.rfb_server import RfbServer, RfbConnectionThread


class LocalTestRfbServerFeature(balder.Feature):
    """setup only feature that provides the bindings for the shipped :class:`RfbServer`"""
    server = None
    config = RfbServerConfig()

    def start_server(self):
        """
        method that starts the rfb server
        """
        self.server = RfbServer(self.config.hostname, self.config.port)
        self.server.start()

    def set_protocol_version(self, protocol_bytes: Union[bytes, bytearray]):
        """
        This method sets the protocol version in the server

        :param protocol_bytes: the protocol that should be returned by the server
        """

        def cb_custom_send_protocol_version(cnn: RfbConnectionThread, received_data: bytes):
            cnn.register_new_expected_msg(12, 'handshake-recv-protocol-version')
            cnn.sock.send(protocol_bytes)

        self.server.register_cb_for_next_upcoming_connection(
            'handshake-send-protocol-version', cb_custom_send_protocol_version)

    def set_security_types(self, security_types: List[int]):
        """
        This method sets the security types that should be returned as available-security-types

        :param security_types: a list with all security types that should be returned
        """
        self.server.filter_available_security_types_for_next_upcoming_connection(security_types)

    def set_security_result(self, security_result: bytes):
        """
        This method sets the security result that should be returned by the rfb server

        :param security_result: the security type that should be returned
        """

        def cb_custom_handshake_send_security_result(cnn: RfbConnectionThread, received_data: bytes):
            cnn.sock.send(security_result)
            cnn.send_conn_failed_msg(f'the BalderHub test server set the security result to {security_result} '
                                     f'(failed)'.encode('ascii'))

        self.server.register_cb_for_next_upcoming_connection(
            'handshake-send-security-result', cb_custom_handshake_send_security_result)

    def set_password(self, password: str):
        """
        This method sets the password in the rfb server.

        :param password: the password that should be set
        """
        self.server.password = password

    def shutdown_server(self):
        """
        This method shuts down the server
        """
        if self.server is not None:
            self.server.shutdown(timeout=60)
        self.server = None
