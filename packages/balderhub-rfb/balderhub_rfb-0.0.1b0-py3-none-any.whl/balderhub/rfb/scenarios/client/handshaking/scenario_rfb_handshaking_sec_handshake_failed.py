import balder
from balderhub.rfb.lib.connections import RfbConnection
from balderhub.rfb.lib.exceptions import RfbClientSecResultFailed
from balderhub.rfb.lib.features.server import RunningRfbServerFeature, RfbServerConfig, SecurityTypeInjectorFeature, \
    PasswordSetterFeature, SecResultInjectorFeature
from balderhub.rfb.lib.features.client import RfbClientFeature, ErrorMessageViewerFeature, RfbClientErrorMessageConfig


class ScenarioRfbHandshakingSecHandshakeFailed(balder.Scenario):
    """
    This test scenario provides tests, that validate if the client works expected in case that the server send a failed
    security handshake.
    """

    class RfbServer(balder.Device):
        """the rfb server device"""
        _ = RunningRfbServerFeature()
        config = RfbServerConfig()
        sec_type_selector = SecurityTypeInjectorFeature()
        password_setter = PasswordSetterFeature()
        sec_result_failed_injector = SecResultInjectorFeature()

    @balder.connect(RfbServer, over_connection=RfbConnection)
    class RfbClient(balder.Device):
        """the rfb client device"""
        rfb_connect = RfbClientFeature(RfbServer="RfbServer")
        error_message_config = RfbClientErrorMessageConfig()
        error_message_viewer = ErrorMessageViewerFeature()

    def test_server_returns_no_security_type(self):
        """
        This test method validates that the client works as expected, while the server sends a security type 1 (FAILED).
        It expects that the client shows the error message that was created and sent by the server.
        The client will be forced to use the security type 2 (VNC-AUTH), because the server only allows this method.
        """
        # set security result to 1 (=FAILED)
        self.RfbServer.sec_result_failed_injector.set_security_result(b'\x00\x00\x00\x01')
        self.RfbServer.password_setter.set_password(self.RfbServer.config.password)
        self.RfbServer.sec_type_selector.set_one_security_type(2)
        try:
            self.RfbClient.rfb_connect.connect(self.RfbServer.config.password)
            assert False, f'connection could be established while server sent security type 0 (INVALID) - this ' \
                          f'should not work'
        except RfbClientSecResultFailed:
            assert self.RfbClient.error_message_config.failed_sec_result == \
                   self.RfbClient.error_message_viewer.get_message()
