from typing import Optional

import balder
from ..server.rfb_server_config import RfbServerConfig


class RfbClientFeature(balder.Feature):
    """feature class that manages the rfb client"""

    class RfbServer(balder.VDevice):
        """vdevice of the rfb server which holds at least the rfb server configuration"""
        config = RfbServerConfig()

    def connect(self, password: Optional[str] = None):
        """
        triggers the rfb client connect

        :param password: the rfb password that should be used for connecting with the rfb server (if this parameter is
                         None, the client should use the password from the configured value in the VDevice)
        """

    def disconnect(self):
        """
        triggers the disconnecting from the connected rfb server
        """
