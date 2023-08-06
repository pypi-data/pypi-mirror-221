from balderhub.rfb.lib import features
from .local_test_rfb_server_feature import LocalTestRfbServerFeature


class PasswordSetterFeature(features.server.PasswordSetterFeature):
    """
    setup feature that sets the password for the shipped :class:`RfbServer`
    """

    server = LocalTestRfbServerFeature()

    def set_password(self, password: str):
        self.server.set_password(password)
