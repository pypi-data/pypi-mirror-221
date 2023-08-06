from typing import Union
import balder


class ErrorMessageViewerFeature(balder.Feature):
    """Feature that allows to access the provided error message from the rfb client"""

    def get_message(self) -> Union[str, None]:
        """
        :return: returns the expected error message
        """
        raise NotImplementedError()
