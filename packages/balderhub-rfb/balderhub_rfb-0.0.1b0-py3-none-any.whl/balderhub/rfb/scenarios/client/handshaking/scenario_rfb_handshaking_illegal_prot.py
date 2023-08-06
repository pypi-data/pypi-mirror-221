import balder
from balderhub.rfb.lib.connections import RfbConnection
from balderhub.rfb.lib.features.server import RunningRfbServerFeature, RfbServerConfig, SecurityTypeInjectorFeature, \
    PasswordSetterFeature, ProtocolInjectorFeature
from balderhub.rfb.lib.features.client import RfbClientFeature


class ScenarioRfbHandshakingIllegalProt(balder.Scenario):
    """
    This scenario tests the client device if it continues with the protocol version 3.3 in case the server sends an
    invalid protocol.
    """

    ILLEGAL_PROTOCOL = b'002.321\n'

    class RfbServer(balder.Device):
        """the rfb server device"""
        _ = RunningRfbServerFeature()
        config = RfbServerConfig()
        sec_type_selector = SecurityTypeInjectorFeature()
        password_setter = PasswordSetterFeature()
        protocol_injector = ProtocolInjectorFeature()

    @balder.connect(RfbServer, over_connection=RfbConnection)
    class RfbClient(balder.Device):
        """the rfb client device"""
        rfb_connect = RfbClientFeature(RfbServer="RfbServer")

    def test_server_returns_illegal_rfb_protocol(self):
        """
        This scenario test method ensures that the client continues with a valid protocol version 3.3 in case the server
        sends an invalid one (test uses  ``002.321``).

        .. note::
            Please note that the current implementation does not verify if the client knows about the protocol version
            3.3. This test will be extended soon.
        """
        self.RfbServer.protocol_injector.set_protocol_version(self.ILLEGAL_PROTOCOL)
        self.RfbServer.password_setter.set_password(self.RfbServer.config.password)
        self.RfbServer.sec_type_selector.set_one_security_type(2)

        self.RfbClient.rfb_connect.connect(password=self.RfbServer.config.password)
        self.RfbClient.rfb_connect.disconnect()
