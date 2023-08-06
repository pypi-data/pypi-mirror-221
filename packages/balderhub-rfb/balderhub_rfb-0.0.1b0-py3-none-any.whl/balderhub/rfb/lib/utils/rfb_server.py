from __future__ import annotations

import random
from typing import Tuple, Union, List, Dict, Callable

import re
import time
import logging
import socket
from Crypto.Cipher import DES
from .tcp_server import TcpThreadedServer, TcpConnectionThread

logger = logging.getLogger(__name__)


class RfbConnectionThread(TcpConnectionThread):

    #: holds the callbacks of all registered security callbacks (sends 0 if there are no!)
    SECURITY_TYPE_CALLABLES: Dict[int, str] = {
        1: 'handshake-auth-none',
        2: 'handshake-auth-vnc'
    }

    #: holds all supported protocol versions
    SUPPORTED_PROTOCOL_VERSIONS = [(3, 3), (3, 7), (3, 8)]

    #: holds the password that should be used by the server
    PASSWORD = None

    def __init__(self, server: RfbServer, sock: socket.socket, address_info: Tuple[str, int]):
        super().__init__(server, sock, address_info)
        self._server = server

        #: holds the amount of bytes that are expected and the callable that should handle the message after it arrives
        self._wait_for_msg: Union[Tuple[int, str], None] = None
        self._wait_for_msg_start_time: float = 0

        #: holds the agreed active protocol version
        self._agreed_protocol_version: Union[Tuple[int, int], Tuple[None, None]] = (None, None)

        #: holds the used security as soon as this was communicated
        self._used_sec_type = None

        #: holds all received data (will be managed by :meth:`handle_new_message()`
        self._data_buffer = b''

        #: holds the send challenge or `None` if no challenge was sent to client
        self.challenge = None

        #: holds the security result of this connection
        self.security_result = 0

    def run(self):
        self.register_new_expected_msg(0, 'handshake-send-protocol-version')
        super().run()

    def register_new_expected_msg(self, byte_count: Union[int, None], callback: str):
        """
        Method that registers a new expected message

        :param byte_count: holds the count of bytes, the incoming message has
        :param callback: holds the callback that should be executed as soon as bytes was received
        """
        logger.debug(f'register new expected message `{callback}` (expected bytes: {byte_count})')
        self._wait_for_msg_start_time = time.perf_counter()
        self._wait_for_msg = (byte_count, callback)

    def handle_new_message(self, data: bytes):
        self._data_buffer += data
        self.handle_rfb_messages()

    def handle_no_message(self):
        self.handle_rfb_messages()

    def handle_rfb_messages(self):
        """callback that will be executed for every incoming rfb message"""
        if self._wait_for_msg:
            byte_count, callback_str = self._wait_for_msg
            if callback_str not in self.CALLBACKS:
                raise KeyError(f'can not find callback key `{callback_str}` - do you have registered it?')

            callback = self.CALLBACKS[callback_str]
            if len(self._data_buffer) > byte_count:
                raise ValueError(f'received more bytes ({len(self._data_buffer)}) than expected ({byte_count})')
            if len(self._data_buffer) == byte_count:
                # we have accepted the wait-for callback
                self._wait_for_msg = None

                for_this_message_relevant = self._data_buffer[:byte_count]
                self._data_buffer = self._data_buffer[byte_count:]
                logger.debug(f'start executing callback `{callback.__name__}` (identifier: `{callback_str}`)')
                callback(self, for_this_message_relevant)
                logger.debug(f'finish executing callback `{callback.__name__}` (identifier: `{callback_str}`)')
            # do nothing when it is fewer data

    ####################################################################################################################
    # RFB HANDSHAKING                                                                                                  #
    ####################################################################################################################

    # pylint: disable-next=unused-argument
    def cb_default_handshake_send_protocol_version(self, received_data: bytes):
        """
        Default callback method that will be executed as soon as the server should send the protocol version

        :param received_data: the received data from the previous message
        """
        self.register_new_expected_msg(12, 'handshake-recv-protocol-version')
        self.sock.send(b"RFB 003.008\n")

    def cb_default_handshake_recv_protocol_version(self, received_data: bytes):
        """
        Default callback method that will be executed as soon as the client should answer with the selected protocol
        version

        :param received_data: the received data from the previous message
        """
        protocol_re = re.compile(b'^RFB (\d{3}).(\d{3})\n$')
        match = protocol_re.match(received_data)
        if not match:
            raise ValueError(f'receive value `{received_data}` that does not fit the regular expression for the '
                             f'protocol version')
        self._agreed_protocol_version = (int(match[1]), int(match[2]))
        if self._agreed_protocol_version not in self.SUPPORTED_PROTOCOL_VERSIONS:
            raise ValueError(f'the server does not support returned version `{self._agreed_protocol_version}` '
                             f'(supported: `{self.SUPPORTED_PROTOCOL_VERSIONS}`) - the RFC6143 describes that the '
                             f'client should use version 3.3 as fallback')
        if self._agreed_protocol_version == (3, 3):
            self.register_new_expected_msg(0, 'handshake-send-security-type-3.3')
        else:
            self.register_new_expected_msg(0, 'handshake-send-available-security-types')

    # pylint: disable-next=unused-argument
    def cb_default_handshake_send_available_security_types(self, received_data: bytes):
        """
        Default callback method that will be executed as soon as the server should send the available security types

        :param received_data: the received data from the previous message
        """
        self.register_new_expected_msg(1, 'handshake-recv-selected-security-type')
        self.sock.send(bytes([len(self.SECURITY_TYPE_CALLABLES),
                              *sorted(self.SECURITY_TYPE_CALLABLES.keys())]))
        if len(self.SECURITY_TYPE_CALLABLES) == 0:
            self.send_conn_failed_msg('No one has set any security types in the BalderHub test server'.encode('ascii'))

    # pylint: disable-next=unused-argument
    def cb_default_handshake_send_security_type_3_3(self, received_data: bytes):
        """
        Default callback method that will be executed if the server only allows the security type 3.3 and as soon as it
        needs to send it

        :param received_data: the received data from the previous message
        """
        if len(self.SECURITY_TYPE_CALLABLES) != 1:
            raise ValueError('can not select a security type, because there is not exactly one (v003.003 needs '
                             'exactly one security type)')
        sec_type, sec_type_callable = self.SECURITY_TYPE_CALLABLES.popitem()
        self.register_new_expected_msg(0, sec_type_callable)
        self.sock.send(int(sec_type).to_bytes(length=4, byteorder='big'))

    def cb_default_handshake_recv_selected_security_type(self, received_data: bytes):
        """
        Default callback method that will be executed as soon as the client should answer with the selected security
        type

        :param received_data: the received data from the previous message
        """
        self._used_sec_type = int(received_data[0])

        if self._used_sec_type in self.SECURITY_TYPE_CALLABLES.keys():
            self.register_new_expected_msg(0, self.SECURITY_TYPE_CALLABLES[self._used_sec_type])
        else:
            raise ValueError(f'the security type `{self._used_sec_type}` is not supported by the server')

    # ----------------
    # RFB AUTH METHODS
    # ----------------

    # note that these callbacks have to be assigned before the server is started, otherwise no security types will be
    # sent!

    # pylint: disable-next=unused-argument
    def cb_default_handle_auth_none(self, received_data: bytes):
        if self._agreed_protocol_version in [(3, 3), (3, 7)]:
            self.register_new_expected_msg(1, 'initialize-recv-client-init')
        else:
            self.register_new_expected_msg(0, 'handshake-send-security-result')

    # pylint: disable-next=unused-argument
    def cb_default_handle_auth_vnc(self, received_data: bytes):
        self.register_new_expected_msg(0, 'handshake-send-auth-vnc-challenge')

    # pylint: disable-next=unused-argument
    def cb_default_send_auth_vnc_challenge(self, received_data: bytes):
        self.challenge = random.randbytes(16)
        self.register_new_expected_msg(16, 'handshake-recv-auth-vnc-password')
        self.sock.send(self.challenge)

    def cb_default_recv_auth_vnc_password(self, received_data: bytes):
        if self.validate_password(encrypted_bytes=received_data):
            if self._agreed_protocol_version in [(3, 3), (3, 7)] and self._used_sec_type == 2:
                # continue with the init message
                self.register_new_expected_msg(1, 'initialize-recv-client-init')
            else:
                # continue with the security result message
                self.register_new_expected_msg(0, 'handshake-send-security-result')
        else:
            # password validation
            self.security_result = 1  # password validation failed!!!
            self.register_new_expected_msg(0, 'handshake-send-security-result')

    # pylint: disable-next=unused-argument
    def cb_default_handshake_send_security_result(self, received_data: bytes):
        if self.security_result == 0:
            self.register_new_expected_msg(1, 'initialize-recv-client-init')
        self.sock.send(self.security_result.to_bytes(length=4, byteorder='big'))
        if self.security_result == 1:
            self.send_conn_failed_msg('invalid credentials detected'.encode('ascii'))

    ####################################################################################################################
    # RFB INITIALIZATION                                                                                               #
    ####################################################################################################################

    # pylint: disable-next=unused-argument
    def cd_default_initialize_recv_client_init(self, received_data: bytes):
        self.register_new_expected_msg(0, 'initialize-send-server-init')

    # pylint: disable-next=unused-argument
    def cb_default_initialize_send_server_init(self, received_data: bytes):
        # todo send server-init message
        self.sock.send(b'\0'*24)

    ####################################################################################################################
    # FURTHER MESSAGES                                                                                                 #
    ####################################################################################################################

    @staticmethod
    def __reorder_pw(password: bytes):
        """
        Helper method to reorder the password according the rfb specification

        :param password: the password in the normal order
        :return: the reordered password
        """
        reordered_pw = []
        for cur_byte_idx, _ in enumerate(password):
            cur_byte_val = ord(password[cur_byte_idx])
            new_byte_val = 0
            for i in range(8):
                if cur_byte_val & (1 << i):
                    new_byte_val = new_byte_val | (1 << 7 - i)
            reordered_pw.append(new_byte_val)
        return bytearray(reordered_pw)

    def validate_password(self, encrypted_bytes: bytes):
        """
        RFB protocol for authentication requires client to encrypt challenge sent by server with password using DES
        method. However, bits in each byte of the password are put in reverse order before using it as encryption key
        (MSB is required).

        :param encrypted_bytes: the received encrypted bytes

        :return: True if the encrypted bytes are valid
        """
        reordered_pw = (self.PASSWORD + '\0' * 8)[:8]  # make sure its 8 chars long (fill with zeros)
        reordered_pw = RfbConnectionThread.__reorder_pw(reordered_pw)
        crypter = DES.new(reordered_pw, DES.MODE_ECB)
        response = crypter.encrypt(self.challenge)
        return response == encrypted_bytes

    def send_conn_failed_msg(self, msg: bytes = None, close_connection: bool = True):
        """
        This method sends a rfb failed message and terminates the connection thread (in case `close_connection` is True)

        :param msg: the message text that should be send
        :param close_connection: True if the thread should terminate after sending the error message
        """
        self.sock.send(len(msg).to_bytes(length=4, byteorder='big') + msg)
        if close_connection:
            self.trigger_stop()

    ####################################################################################################################
    # DEFAULT CALLBACKS                                                                                                #
    ####################################################################################################################

    # pylint: disable-next=fixme
    # TODO can we use dataclasses here? maybe we can group them?
    CALLBACKS = {
        'handshake-send-protocol-version': cb_default_handshake_send_protocol_version,
        'handshake-recv-protocol-version': cb_default_handshake_recv_protocol_version,
        'handshake-send-available-security-types': cb_default_handshake_send_available_security_types,
        'handshake-send-security-type-3.3': cb_default_handshake_send_security_type_3_3,
        'handshake-recv-selected-security-type': cb_default_handshake_recv_selected_security_type,
        'handshake-auth-none': cb_default_handle_auth_none,
        'handshake-auth-vnc': cb_default_handle_auth_vnc,
        'handshake-send-auth-vnc-challenge': cb_default_send_auth_vnc_challenge,
        'handshake-recv-auth-vnc-password': cb_default_recv_auth_vnc_password,
        'handshake-send-security-result': cb_default_handshake_send_security_result,
        'initialize-recv-client-init': cd_default_initialize_recv_client_init,
        'initialize-send-server-init': cb_default_initialize_send_server_init
    }


class RfbServer(TcpThreadedServer):
    """threaded rfb test server"""
    CNN_HANDLER_THREAD_CLS = RfbConnectionThread

    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.available_security_types = None
        self.next_callbacks = {}
        self.password = None

    def handle_new_connection(self, sock, client_host, client_port):
        thread: RfbConnectionThread = self._create_new_connection_thread(sock, client_host, client_port)

        # handle custom callbacks if they exists
        thread.CALLBACKS = {**thread.CALLBACKS, **self.next_callbacks}
        self.next_callbacks = {}

        # set the connection password
        thread.PASSWORD = self.password

        # handle the available security type filter
        if self.available_security_types is not None:
            # filter is active
            remaining = {}
            for cur_type in self.available_security_types:
                if cur_type not in thread.SECURITY_TYPE_CALLABLES.keys():
                    raise KeyError(f'there is no callback defined in the connection thread for security-type '
                                   f'{cur_type}')
                remaining[cur_type] = thread.SECURITY_TYPE_CALLABLES[cur_type]
            thread.SECURITY_TYPE_CALLABLES = remaining

        self._start_thread(sock, thread)

    def register_cb_for_next_upcoming_connection(
            self, cb_key: str, cb_function: Callable[[RfbConnectionThread, bytes], None]):
        """
        This method allows to register a custom callback for the next incoming connection.

        :param cb_key: the callback key
        :param cb_function: the callback function
        """
        self.next_callbacks[cb_key] = cb_function

    def filter_available_security_types_for_next_upcoming_connection(self, available_types: List[int]):
        """
        This method filters the available security types for the next upcoming connection. This makes it possible to
        specify which security types the server should support in the next connection.

        :param available_types: a list of all remaining available security types
        """
        self.available_security_types = available_types
