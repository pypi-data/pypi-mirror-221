from balderhub.rfb.lib import features
from .local_test_rfb_server_feature import LocalTestRfbServerFeature


class SecResultInjectorFeature(features.server.SecResultInjectorFeature):
    """
    setup feature that allows to set inject a security result that should be returned by the shipped :class:`RfbServer`
    """

    server = LocalTestRfbServerFeature()

    def set_security_result(self, security_result: bytes):
        self.server.set_security_result(security_result)
