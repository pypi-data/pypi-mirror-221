import balder


class ClosedPortConfig(balder.Feature):
    """config feature that returns a port that is expected to be closed"""

    def get_closed_port(self) -> int:
        """
        :return: returns an expected closed port
        """
        raise NotImplementedError()
