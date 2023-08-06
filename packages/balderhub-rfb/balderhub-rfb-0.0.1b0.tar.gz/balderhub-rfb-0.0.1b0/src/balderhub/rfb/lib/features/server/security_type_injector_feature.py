from typing import Union

import balder


class SecurityTypeInjectorFeature(balder.Feature):
    """feature that sets the allowed security types that should be returned by the server"""

    def set_one_security_type(self, security_type: Union[int, None]):
        """
        This method allows to set exactly one allowed security type. This value will be returned by the server in the
        available-security-type message.

        :param security_type: the security type that should be set in the server (None in case the server should return
                              no 'supported security types')
        """
        raise NotImplementedError()
