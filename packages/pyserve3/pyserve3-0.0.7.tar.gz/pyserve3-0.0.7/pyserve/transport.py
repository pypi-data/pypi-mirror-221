"""
AsyncIO Implementations of session-based servers
"""
import asyncio
from ssl import SSLContext
from typing import Type, Optional, Dict, Any, Protocol

from pyderive import dataclass, field

from .abc import * 

#** Variables **#
__all__ = ['UdpProtocol', 'TcpProtocol']

#** Classes **#

class BaseWriter(Writer, Protocol):
    transport: asyncio.Transport
 
    def using_tls(self) -> bool:
        return 'ssl' in self.transport.__class__.__name__.lower()

    def start_tls(self, context: SSLContext):
        protocol  = self.transport.get_protocol()
        loop      = asyncio.get_event_loop()
        future    = loop.start_tls(
            transport=self.transport,
            protocol=protocol,
            sslcontext=context,
            server_side=True,
        )
        def callback(task: asyncio.Task):
            self.transport = task.result()
        task = loop.create_task(future)
        task.add_done_callback(callback)

    def close(self):
        self.transport.close()

    def is_closing(self) -> bool:
        return self.transport.is_closing()

@dataclass(slots=True)
class UdpWriter(UdpWriter, BaseWriter):
    addr:      Address
    transport: asyncio.DatagramTransport 
 
    def start_tls(self, context: SSLContext):
        raise NotImplementedError('Cannot Use SSL over UDP')

    def write(self, data: bytes, addr: Optional[AnyAddr] = None):
        self.transport.sendto(data, addr or self.addr)

@dataclass(slots=True)
class TcpWriter(BaseWriter):
    transport: asyncio.Transport 

    def write(self, data: bytes):
        self.transport.write(data)

@dataclass
class BaseProtocol:
    factory:   Type[Session]
    args:      tuple           = field(default_factory=tuple)
    kwargs:    Dict[str, Any]  = field(default_factory=dict)

    def test_factory(self):
        """validate session can be generated w/ args and kwargs"""
        self.factory(*self.args, **self.kwargs)

    def set_timeout(self, timeout: int, tport: asyncio.Transport):
        """implement timeout handling for async servers"""
        # generate async expiration function
        async def expire():
            await asyncio.sleep(timeout)
            if not tport.is_closing():
                tport.abort()
        # spawn future to kill transport
        loop = asyncio.get_event_loop()
        loop.create_task(expire())

class UdpProtocol(BaseProtocol, asyncio.DatagramTransport):
 
    def connection_made(self, transport: asyncio.DatagramTransport):
        """"""
        # handle modifying socket and making changes for handling
        self.transport = transport
 
    def datagram_received(self, data: bytes, addr: RawAddr):
        """"""
        # generate session w/ attributes and notify on connection-made
        address      = Address(*addr)
        writer       = UdpWriter(address, self.transport)
        self.session = self.factory(*self.args, **self.kwargs)
        self.session.connection_made(address, writer)
        self.session.data_recieved(data)

    def connection_lost(self, err: Optional[Exception]):
        """"""
        self.session.connection_lost(err)

@dataclass
class TcpProtocol(BaseProtocol, asyncio.Protocol):
    timeout: Optional[int] = None
   
    def connection_made(self, transport: asyncio.Transport):
        """"""
        # collect attributes and prepare socket for session
        address = Address(*transport.get_extra_info('peername'))
        # handle modifying socket and making changes for handling
        if self.timeout is not None:
            self.set_timeout(self.timeout, transport)
        # generate session w/ attributes and notify on connection-made
        self.session = self.factory(*self.args, **self.kwargs)
        self.session.connection_made(address, TcpWriter(transport))

    def data_received(self, data: bytes):
        """"""
        self.session.data_recieved(data)

    def connection_lost(self, err: Optional[Exception]):
        """"""
        self.session.connection_lost(err)
