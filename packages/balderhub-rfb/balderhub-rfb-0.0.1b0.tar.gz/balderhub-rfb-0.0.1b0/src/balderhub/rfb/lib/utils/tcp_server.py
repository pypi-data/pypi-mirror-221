from __future__ import annotations

import time
from typing import List, Tuple, Union
import select
import socket
import logging
from threading import Thread, Event

logger = logging.getLogger(__name__)


class ClientThreadException(Exception):
    pass


class TcpConnectionThread(Thread):
    """
    Helper thread for every new tcp connection
    """

    RECV_BUFFER_SIZE_BYTES = 1024

    def __init__(self, server, sock: socket.socket, address_info: Tuple[str, int]):
        """
        creates a new tcp connection thread object

        :param server: the server object that belongs to this connection thread

        :param sock: the connection socket

        :param address_info: the information tuple of the connected client
        """
        super().__init__()
        self._server = server
        self.sock = sock
        self._address_info = address_info

        self.name = f"TcpConnectionThread<{self.client_host}:{self.client_port}>"

        self._terminate_event = Event()

        self._thread_exc: Union[BaseException, None] = None

    @property
    def client_host(self) -> str:
        """
        :return: returns the host of the connection client
        """
        return self._address_info[0]

    @property
    def client_port(self) -> int:
        """
        :return: returns the port of the connection client
        """
        return self._address_info[1]

    @property
    def thread_exc(self) -> Union[BaseException, None]:
        """
        :return: holds the exception that was thrown in the thread (or None if there was no exception in the thread yet)
        """
        return self._thread_exc

    def run(self):
        """the threaded method"""
        logger.debug(f'start server connection thread `{self.name}`')
        try:

            try:
                while not self._terminate_event.is_set():

                    readable, _, _ = select.select([self.sock], [self.sock], [], 0.01)

                    if readable:
                        data = self.sock.recv(self.RECV_BUFFER_SIZE_BYTES)
                        logger.debug(f'receive data `{data}` (len: {len(data)})')
                        if data:
                            self.handle_new_message(data)
                        else:
                            break
                    else:
                        self.handle_no_message()
                    # todo also add the send process here
            finally:
                logger.debug(f'close client socket for connection `{self.client_host}:{self.client_port}`')
                self.sock.close()

        except BaseException as exc:
            self._thread_exc = exc
            raise exc

        finally:
            logger.debug(f'terminate tcp-server connection thread `{self.name}`')

    def trigger_stop(self):
        """will trigger the stop process for this thread"""
        self._terminate_event.set()

    def handle_new_message(self, data: bytes):
        """method that will be called in case a new message arrived"""

    def handle_no_message(self):
        """callback method that will be triggered for every iteration at which no message was received"""


class TcpThreadedServer(Thread):
    """
    Helper thread for a tcp server
    """

    #: the connection thread class that should be created for every new connection
    CNN_HANDLER_THREAD_CLS = TcpConnectionThread

    def __init__(self, host: str, port: int):
        """
        creates a new server object

        :param host: the host of the server
        :param port: the port of the server
        """
        super().__init__()
        self._host = host
        self._port = port
        self._clients: List[Tuple[socket.socket, TcpConnectionThread]] = []
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.setblocking(False)

        self.name = f"TcpThreadedServer<{self.host}:{self.port}>"

        self._terminate_event = Event()
        self._running_event = Event()

        self._thread_exc: Union[BaseException, None] = None

    @property
    def host(self) -> str:
        """
        :return: returns the host of the tcp server
        """
        return self._host

    @property
    def port(self) -> int:
        """
        :return: returns the port of the tcp server
        """
        return self._port

    @property
    def thread_exc(self) -> Union[BaseException, None]:
        """
        :return: holds the exception that was thrown in the thread (or None if there was no exception in the thread yet)
        """
        return self._thread_exc

    def start(self) -> None:
        """starts the thread"""
        super().start()

        self.wait_till_thread_loop_is_active()

    def wait_till_thread_loop_is_active(self, timeout=10):
        """
        waits for the thread loop to terminate

        :param timeout: max time this method will block
        """
        start_time = time.perf_counter()
        while True:
            if self._running_event.is_set():
                break
            if (time.perf_counter() - start_time) > timeout:
                raise TimeoutError(f'thread does not switch into running mode after {timeout} seconds')

    def run(self):
        """the threaded method"""

        logger.debug(f'start server thread `{self.name}')

        try:

            try:
                # bind the socket to its host and port
                self._sock.bind((self.host, self.port))

                # start listening for a client
                self._sock.listen(1)

                while not self._terminate_event.is_set():
                    self._running_event.set()

                    readable, _, _ = select.select([self._sock], [self._sock], [], 1)

                    if readable:
                        client, address_info = self._sock.accept()
                        client.setblocking(False)
                        self.handle_new_connection(client, *address_info)
                        logger.debug(f'new incoming connection from `{address_info[0]}:{address_info[1]}`')
                self._running_event.clear()

            finally:
                logger.debug(f'receive terminate event - close main tcp server socket of thread `{self.name}` now')
                self._sock.close()

        except BaseException as exc:
            self._thread_exc = exc
            raise exc

        finally:
            logger.debug(f'terminate server thread `{self.name}`')

    def _create_new_connection_thread(self, sock, client_host, client_port):
        """
        Callback that will create a new conneciton thread

        :param sock: the connection socket
        :param client_host: the host of the remote client of this connection
        :param client_port: the port of the remote client of this connection
        :return: the new connection thread object
        """
        return self.CNN_HANDLER_THREAD_CLS(self, sock, (client_host, client_port))

    def _start_thread(self, sock, thread):
        """
        callback method that will be executed to start a new connection thread

        :param sock: the connection socket
        :param thread: the connection thread
        """
        # start a thread to listen to the client
        thread.start()

        # add client to list
        self._clients.append((sock, thread))

    def handle_new_connection(self, sock, client_host, client_port):
        """
        callback method that handles a new incoming connection

        :param sock: the connection socket
        :param client_host: the remote client host
        :param client_port: the remote client port
        """

        thread = self._create_new_connection_thread(sock, client_host, client_port)
        self._start_thread(sock, thread)

    def shutdown(self, timeout: float):
        """

        .. note::
            The timeout should be higher than 1, because the inner select uses a timeout of 1 second

        :param timeout: max time this method will block
        """

        # close the current connection
        self._terminate_event.set()

        # close all client connections
        for _, client_thread in self._clients:
            client_thread.trigger_stop()

        start_time = time.perf_counter()

        # now wait for all the client threads to terminate
        for _, client_thread in self._clients:
            rel_timeout = max(timeout - (time.perf_counter() - start_time), 0.1)
            client_thread.join(timeout=rel_timeout)

        # if there is any thread that does not terminate yet, the upcoming timout error will be thrown
        rel_timeout = max(timeout - (time.perf_counter() - start_time), 0.1)
        # now wait for the main thread
        self.join(timeout=rel_timeout)

        # check for thread exceptions
        for _, client_thread in self._clients:
            if client_thread.thread_exc is not None:
                raise ClientThreadException(f'the client thread `{client_thread.name}` of tcp server thread '
                                            f'`{self.name}` has thrown an exception') from client_thread.thread_exc

        # check that no client threads are alive anymore
        for _, client_thread in self._clients:
            if self.is_alive():
                raise TimeoutError(f'client thread `{client_thread.name}` is still alive after join')

        if self.thread_exc is not None:
            raise ClientThreadException(f'the tcp server thread `{self.name}` has thrown an exception') from \
                self.thread_exc

        if self.is_alive():
            raise TimeoutError(f'main tcp server thread `{self.name}` is still active after join')
