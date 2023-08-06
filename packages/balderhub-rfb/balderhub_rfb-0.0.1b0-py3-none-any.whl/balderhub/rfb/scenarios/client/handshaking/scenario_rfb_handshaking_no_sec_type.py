import time

import balder
from balderhub.rfb.lib.connections import RfbConnection
from balderhub.rfb.lib.exceptions import RfbClientHandshakeSecurityTypeFailed
from balderhub.rfb.lib.features.server import RunningRfbServerFeature, RfbServerConfig, SecurityTypeInjectorFeature
from balderhub.rfb.lib.features.client import RfbClientFeature, ErrorMessageViewerFeature, RfbClientErrorMessageConfig


class ScenarioRfbHandshakingNoSecType(balder.Scenario):
    """
    This scenario provides tests that checks if the client work as expected in case no-security type will be returned
    by the server.
    """

    class RfbServer(balder.Device):
        """the rfb server device"""
        _ = RunningRfbServerFeature()
        config = RfbServerConfig()
        sec_type_selector = SecurityTypeInjectorFeature()

    @balder.connect(RfbServer, over_connection=RfbConnection)
    class RfbClient(balder.Device):
        """the rfb client device"""
        rfb_connect = RfbClientFeature(RfbServer="RfbServer")
        error_message_config = RfbClientErrorMessageConfig()
        error_message_viewer = ErrorMessageViewerFeature()

    def test_server_returns_no_security_type(self):
        """
        This test method validates if the server provides the error message that was set by the server, because it sends
        no supported security types. The client should provide the error message that was sent by the server.
        """
        # set no available security types
        self.RfbServer.sec_type_selector.set_one_security_type(None)
        try:
            self.RfbClient.rfb_connect.connect()
            time.sleep(1)
            assert False, 'connection could be established while server sent security type 0 (INVALID) - this ' \
                          'should not work'

        except RfbClientHandshakeSecurityTypeFailed:
            assert self.RfbClient.error_message_config.invalid_security_type == \
                   self.RfbClient.error_message_viewer.get_message()
