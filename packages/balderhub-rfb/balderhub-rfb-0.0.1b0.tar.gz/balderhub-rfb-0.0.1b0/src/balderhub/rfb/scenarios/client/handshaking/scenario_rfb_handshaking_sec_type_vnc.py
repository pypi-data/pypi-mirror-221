import balder
from balderhub.rfb.lib.connections import RfbConnection
from balderhub.rfb.lib.features.server import RunningRfbServerFeature, RfbServerConfig, SecurityTypeInjectorFeature, \
    PasswordSetterFeature
from balderhub.rfb.lib.features.client import RfbClientFeature


class ScenarioRfbHandshakingSecTypeVnc(balder.Scenario):
    """
    This scenario holds tests, that validates that the client works as expected by using the security type VNC-AUTH (2).

    In this authentication mode, the rfb specification only considers passwords with length of 8 characters. The
    scenario provides different tests that checks around this border.
    """

    PASSWORD_FULL = "Aa0!'\"j4@9zZ"

    PASSWORD_LESSTHEN8 = PASSWORD_FULL[:6]
    PASSWORD_EQUAL8 = PASSWORD_FULL[:8]

    class RfbServer(balder.Device):
        """the rfb server device"""
        _ = RunningRfbServerFeature()
        config = RfbServerConfig()
        sec_type_selector = SecurityTypeInjectorFeature()
        password_setter = PasswordSetterFeature()

    @balder.connect(RfbServer, over_connection=RfbConnection)
    class RfbClient(balder.Device):
        """the rfb client device"""
        rfb_connect = RfbClientFeature(RfbServer="RfbServer")

    def test_with_auth_vnc_lessthan8chars(self):
        """
        This test method validates that the client works as expected, while the VNC-AUTH password has less than
        8 characters.
        It ensures that the client is able to connect with the server.
        """
        # set security type to 2 (=VNC-AUTHENTICATION)
        self.RfbServer.sec_type_selector.set_one_security_type(2)
        self.RfbServer.password_setter.set_password(self.PASSWORD_LESSTHEN8)

        try:
            self.RfbClient.rfb_connect.connect(password=self.PASSWORD_LESSTHEN8)
        finally:
            self.RfbClient.rfb_connect.disconnect()

    def test_with_auth_vnc_equal8chars(self):
        """
        This test method validates that the client works as expected, while the VNC-AUTH password has exactly
        8 characters.
        It ensures that the client is able to connect with the server.
        """
        # set security type to 2 (=VNC-AUTHENTICATION)
        self.RfbServer.sec_type_selector.set_one_security_type(2)
        self.RfbServer.password_setter.set_password(self.PASSWORD_EQUAL8)

        try:
            self.RfbClient.rfb_connect.connect(password=self.PASSWORD_EQUAL8)
        finally:
            self.RfbClient.rfb_connect.disconnect()

    def test_with_auth_vnc_morethan8chars(self):
        """
        This test method validates that the client works as expected, while the VNC-AUTH password has more than
        8 characters.
        It ensures that the client is able to connect with the server.
        """
        # set security type to 2 (=VNC-AUTHENTICATION)
        self.RfbServer.sec_type_selector.set_one_security_type(2)
        self.RfbServer.password_setter.set_password(self.PASSWORD_FULL)

        try:
            self.RfbClient.rfb_connect.connect(password=self.PASSWORD_FULL)
        finally:
            self.RfbClient.rfb_connect.disconnect()
