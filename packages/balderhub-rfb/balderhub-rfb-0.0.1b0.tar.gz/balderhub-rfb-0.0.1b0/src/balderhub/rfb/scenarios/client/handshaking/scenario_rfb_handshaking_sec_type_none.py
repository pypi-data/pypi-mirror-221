import balder
from balderhub.rfb.lib.connections import RfbConnection
from balderhub.rfb.lib.features.server import RunningRfbServerFeature, RfbServerConfig, SecurityTypeInjectorFeature
from balderhub.rfb.lib.features.client import RfbClientFeature


class ScenarioRfbHandshakingSecTypeNone(balder.Scenario):
    """
    This scenario holds tests, that validates that the client works as expected by using the security type NONE (1).
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

    def test_with_auth_none(self):
        """
        This test method forces the client to use the security type 1 (NO-AUTHENTICATION). It validates that the client
        is able to connect with the server without using any authentification.
        """
        # set security type to 1 (=NO-AUTHENTICATION)
        self.RfbServer.sec_type_selector.set_one_security_type(1)

        try:
            self.RfbClient.rfb_connect.connect()
        finally:
            self.RfbClient.rfb_connect.disconnect()
