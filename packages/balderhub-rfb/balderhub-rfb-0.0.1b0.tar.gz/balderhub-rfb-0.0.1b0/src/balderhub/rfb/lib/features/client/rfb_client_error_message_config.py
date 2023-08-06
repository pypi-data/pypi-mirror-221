import balder


class RfbClientErrorMessageConfig(balder.Feature):
    """config feature that holds information about the expected error messages of the rfb client"""

    @property
    def invalid_security_type(self) -> str:
        """
        :return: return the expected error message if the security type is invalid
        """
        raise NotImplementedError()

    @property
    def failed_sec_result(self) -> str:
        """
        :return: return the expected error message if the security result failed
        """
        raise NotImplementedError()
