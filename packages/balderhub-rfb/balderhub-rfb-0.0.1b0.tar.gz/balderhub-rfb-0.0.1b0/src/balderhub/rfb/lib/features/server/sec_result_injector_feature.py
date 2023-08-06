import balder


class SecResultInjectorFeature(balder.Feature):
    """feature that allows to set inject a security result that should be returned by the rfb server"""

    def set_security_result(self, security_result: bytes):
        """
        This method sets the security result that should be returned by the server (independent of the normal workflow)

        :param security_result: the security result that should be set
        """
        raise NotImplementedError()
