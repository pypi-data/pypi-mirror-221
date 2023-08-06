import balder


class PasswordSetterFeature(balder.Feature):
    """feature that sets the password for the rfb server"""

    def set_password(self, password: str):
        """
        This method sets the password that should be used by the server

        :param password: the password that should be set
        """
        raise NotImplementedError()
