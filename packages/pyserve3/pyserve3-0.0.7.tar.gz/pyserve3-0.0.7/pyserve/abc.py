"""

"""
import socket
from ssl import SSLContext
from abc import abstractmethod
from collections import namedtuple
from typing import Tuple, Protocol, Optional, Union

#** Variables **#
__all__ = [
    'modify_socket',

    'RawAddr',
    'Address',
    'AnyAddr',
    'Writer',
    'UdpWriter',
    'Session',
]

#: raw address tuple
RawAddr = Tuple[str, int]

#: named address tuple
Address = namedtuple('Address', ('host', 'port'))

#: any address tuple
AnyAddr = Union[RawAddr, Address]

#** Functions **#

def modify_socket(
    sock:      socket.socket, 
    timeout:   Optional[int], 
    interface: Optional[str]
) -> socket.socket:
    """
    modify the socket object w/ the following options
    """
    if timeout is not None:
        sock.settimeout(timeout)
    if interface is not None:
        iface = interface.encode()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, iface)
    return sock 

#** Classes **#

class Writer(Protocol):
    """
    abstract data-writing implementation for single server connection
    """
    
    @abstractmethod
    def using_tls(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def start_tls(self, context: SSLContext):
        raise NotImplementedError

    @abstractmethod
    def write(self, data: bytes):
        raise NotImplementedError
    
    @abstractmethod
    def close(self):
        raise NotImplementedError
 
    @abstractmethod
    def is_closing(self) -> bool:
        raise NotImplementedError

class UdpWriter(Writer, Protocol):
    """
    abstract data-writing implementation for udp server connection
    """

    @abstractmethod
    def write(self, data: bytes, addr: Optional[AnyAddr] = None):
        raise NotImplementedError

class Session(Protocol):
    """
    abstract session-manager implemention for single server connection
    """
    
    @abstractmethod
    def connection_made(self, addr: Address, writer: Writer):
       raise NotImplementedError

    @abstractmethod
    def data_recieved(self, data: bytes):
        raise NotImplementedError

    @abstractmethod
    def connection_lost(self, err: Optional[Exception]):
        raise NotImplementedError
