"""
Unify SocketServer Implementations based on Session Model
"""
import asyncio
from ssl import SSLContext
from typing import Type, Optional

from .abc import * 
from .transport import UdpProtocol, TcpProtocol
from .threading import UdpThreadServer, TcpThreadServer

#** Variables **#
__all__ = [
    'listen_udp_async',
    'listen_tcp_async',
    'listen_udp_threaded',
    'listen_tcp_threaded',

    'Address',
    'Writer',
    'UdpWriter',
    'Session',
]

#** Functions **#

async def listen_udp_async(
    address:         RawAddr, 
    factory:         Type[Session],
    *args,
    interface:       Optional[str] = None,
    reuse_port:      bool          = False,
    allow_broadcast: bool          = False,
    **kwargs,
):
    """
    :param address:         host/port of server
    :param factory:         type factory for server request handler
    :param args:            positional args to pass to the session factory
    :param interface:       interface to bind server socket to
    :param reuse_port:      allow reuse of same port when enabled
    :param allow_broadcast: allow for udp broadcast messages when enabled
    :param kwargs:          keyword arguments to pass to session factory
    """
    # spawn protocol factory and test session generation
    loop = asyncio.get_running_loop()
    func = lambda: UdpProtocol(factory, args, kwargs)
    func().test_factory()
    # spawn server instance
    tport, protocol = await loop.create_datagram_endpoint(func, address, 
        reuse_port=reuse_port, allow_broadcast=allow_broadcast)
    # modify transport interface when enabled
    if interface:
        sock = protocol.transport.get_extra_info('socket')
        modify_socket(sock, None, interface)
    # run server forever
    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        tport.close()

async def listen_tcp_async(
    address:    RawAddr, 
    factory:    Type[Session],
    *args,
    timeout:    Optional[int]        = None,
    interface:  Optional[str]        = None,
    reuse_port: bool                 = False,
    backlog:    int                  = 100,
    ssl:        Optional[SSLContext] = None,
    **kwargs,
):
    """
    :param address:         host/port of server
    :param factory:         type factory for server request handler
    :param args:            positional args to pass to the session factory
    :param timeout:         max socket lifetime duration timeout if configured
    :param interface:       interface to bind server socket to
    :param reuse_port:      allow reuse of same port when enabled
    :param backlog:         number of allowed and backloged async requests
    :param ssl:             TLS context to encrypt socket communications
    :param kwargs:          keyword arguments to pass to session factory
    """
    # spawn protocol factory and test session generation
    loop = asyncio.get_running_loop()
    func = lambda: TcpProtocol(factory, args, kwargs, timeout)
    func().test_factory()
    # spawn server instance
    host, port = address
    server = await loop.create_server(func, host, port, 
        reuse_port=reuse_port, backlog=backlog, ssl=ssl)
    # modify interface settings for sockets (when enabled)
    if interface:
        for sock in server.sockets:
            modify_socket(sock, None, interface)
    # run server forever
    async with server:
        await server.serve_forever()

def listen_udp_threaded(
    address:         RawAddr, 
    factory:         Type[Session],
    *args,
    interface:       Optional[str] = None,
    reuse_port:      bool          = False,
    allow_broadcast: bool          = False,
    blocksize:  int                = 8192,
    **kwargs,
):
    """
    :param address:         host/port of server
    :param factory:         type factory for server request handler
    :param args:            positional args to pass to the session factory
    :param timeout:         max socket lifetime duration timeout if configured
    :param interface:       interface to bind server socket to
    :param reuse_port:      allow reuse of same port when enabled
    :param allow_broadcast: allow for udp broadcast messages when enabled
    :param kwargs:          keyword arguments to pass to session factory
    """
    factory(*args, **kwargs)
    server = UdpThreadServer(
        address=address, 
        factory=factory, 
        args=args, 
        kwargs=kwargs, 
        interface=interface,
        blocksize=blocksize,
        reuse_port=reuse_port, 
        allow_broadcast=allow_broadcast,
    )
    with server:
        server.serve_forever()

def listen_tcp_threaded(
    address:    RawAddr,
    factory:    Type[Session],
    *args,
    timeout:    Optional[int]        = None,
    interface:  Optional[str]        = None,
    reuse_port: bool                 = False,
    ssl:        Optional[SSLContext] = None,
    blocksize:  int                  = 8192,
    **kwargs,
):
    """
    :param address:         host/port of server
    :param factory:         type factory for server request handler
    :param args:            positional args to pass to the session factory
    :param timeout:         max socket lifetime duration timeout if configured
    :param interface:       interface to bind server socket to
    :param reuse_port:      allow reuse of same port when enabled
    :param backlog:         number of allowed and backloged async requests
    :param ssl:             TLS context to encrypt socket communications
    :param kwargs:          keyword arguments to pass to session factory
    """
    factory(*args, **kwargs)
    server = TcpThreadServer(
        address=address, 
        factory=factory, 
        args=args, 
        kwargs=kwargs, 
        timeout=timeout, 
        interface=interface, 
        reuse_port=reuse_port, 
        ssl=ssl,
        blocksize=blocksize,
    )
    with server:
        server.serve_forever()
