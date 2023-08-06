import balder


class RfbServerConfig(balder.Feature):
    """config feature that holds all important coniguration of the rfb server"""

    @property
    def hostname(self):
        """
        :return: returns the hostname of the rfb server
        """
        raise NotImplementedError()

    @property
    def port(self):
        """
        :return: returns the port of the rfb server
        """
        raise NotImplementedError()

    @property
    def password(self):
        """
        :return: returns the valid password of the rfb server
        """
        raise NotImplementedError()
