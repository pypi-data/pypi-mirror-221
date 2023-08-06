import balder
from balder.connections import TcpIPv4Connection


@balder.insert_into_tree(parents=[TcpIPv4Connection])
class RfbConnection(balder.Connection):
    """
    special connection for rfb connections
    """
