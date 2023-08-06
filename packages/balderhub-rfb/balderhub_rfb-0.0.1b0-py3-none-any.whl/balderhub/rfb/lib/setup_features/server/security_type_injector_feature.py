from typing import List, Union
from balderhub.rfb.lib import features
from .local_test_rfb_server_feature import LocalTestRfbServerFeature


class SecurityTypeInjectorFeature(features.server.SecurityTypeInjectorFeature):
    """
    setup feature that sets the allowed security types that should be returned by the shipped :class:`RfbServer`
    """

    server = LocalTestRfbServerFeature()

    def set_allowed_security_types(self, security_types: List[int]):
        """note: the set security types must be supported by the server"""
        self.server.set_security_types(security_types)

    def set_one_security_type(self, security_type: Union[int, None]):
        if security_type is None:
            self.server.set_security_types([])
        else:
            self.server.set_security_types([security_type])
