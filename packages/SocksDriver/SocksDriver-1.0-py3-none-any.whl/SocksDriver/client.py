from json import loads
from json.decoder import JSONDecodeError
from typing import Optional
import socket
from SocksDriver.errors import SocksConnectionError, SocksTransmissionError, SocksInternalServerError
from SocksDriver import complex_types


class SocksClient:

    """Client for interfacing with ChristmasSocks servers.

    :param str, optional addr: The address that this client will attempt to connect to. The
        address follows the format: <host:port>. If no address is provided, then the client
        will attempt to connect to localhost:8080.
    """

    TIMEOUT_SECS = 1.5
    BUFFER_SIZE = 16384

    def __init__(self, addr: Optional[str] = None) -> None:

        if addr is None:
            self.addr = 'localhost:8080'
        else:
            self.addr = addr

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.TIMEOUT_SECS)
        self.connected = False

    def connect(self) -> None:

        """Connect to peer specified via the `addr` constructor argument.

        :raise: SocksConnectionError if a connection could not be established.
        """

        try:
            host, port_s = self.addr.split(':')
        except ValueError as exc:
            raise SocksConnectionError('Address must be of form <ip-addr:port>') from exc

        try:
            port = int(port_s)
        except ValueError as exc:
            raise SocksConnectionError('Invalid port parsed from address') from exc

        try:
            self.socket.connect((host, port))
        except socket.timeout as exc:
            raise SocksConnectionError('Server is possibly dead') from exc
        except ConnectionRefusedError as exc:
            raise SocksConnectionError('Server is refusing connections on port') from exc

        self.connected = True

    def disconnect(self) -> None:

        """Disconnect from peer specified via the `addr` constructor argument."""

        self.socket.close()
        self.connected = False

    def send(self, command: str) -> str:

        """Send a string to `addr`.

        :param str command: The message to send to the peer.
        :return str: The message received from the peer.
        :raise: SocksTransmissionError if message could not be sent.
        """

        try:
            self.socket.sendall(command.encode())
        except OSError as exc:
            raise SocksTransmissionError('Connection to server does not exist') from exc

        try:
            bytes_recv = self.socket.recv(self.BUFFER_SIZE)
        except ConnectionError as exc:
            raise SocksTransmissionError('Failed to receive data') from exc

        return bytes_recv.decode()

    def help(self) -> dict[str, str]:

        """Ask peer to list all available ChristmasSocks commands.

        :return dict[str, str]
        :raise: SocksTransmissionError if round-trip transmission failed.
        :raise: SocksInternalServerError if server returns an error.
        """

        results_s = self.send('help')

        try:
            results = loads(results_s)
        except JSONDecodeError as exc:
            raise SocksTransmissionError('Could not decode data. Buffer size is possibly too small') from exc

        if results['status'] != 'Success':
            raise SocksInternalServerError(results['status'])

        del results['status']

        return results

    def uptime(self) -> dict[str, str]:

        """Ask peer to list platform uptime.

        :return dict[str, str]
        :raise: SocksTransmissionError if round-trip transmission failed.
        :raise: SocksInternalServerError if server returns an error.
        """

        results_s = self.send('uptime')

        try:
            results = loads(results_s)
        except JSONDecodeError as exc:
            raise SocksTransmissionError('Could not decode data. Buffer size is possibly too small') from exc

        if results['status'] != 'Success':
            raise SocksInternalServerError(results['status'])

        del results['status']

        return results

    def sysinfo(self) -> dict[str, str]:

        """Ask peer to list platform system information.

        :return dict[str, str]
        :raise: SocksTransmissionError if round-trip transmission failed.
        :raise: SocksInternalServerError if server returns an error.
        """

        results_s = self.send('sysinfo')

        try:
            results = loads(results_s)
        except JSONDecodeError as exc:
            raise SocksTransmissionError('Could not decode data. Buffer size is possibly too small') from exc

        if results['status'] != 'Success':
            raise SocksInternalServerError(results['status'])

        del results['status']

        return results

    def sleep(self) -> dict[str, str]:

        """Ask peer to sleep for short duration.

        :return dict[str, str]
        :raise: SocksTransmissionError if round-trip transmission failed.
        :raise: SocksInternalServerError if server returns an error.
        """

        results_s = self.send('sleep')

        try:
            results = loads(results_s)
        except JSONDecodeError as exc:
            raise SocksTransmissionError('Could not decode data. Buffer size is possibly too small') from exc

        if results['status'] != 'Success':
            raise SocksInternalServerError(results['status'])

        del results['status']

        return results

    def blockdev(self) -> list[complex_types.TYPE_BLOCKDEV]:

        """Ask peer to list information about block devices.

        :return list[TYPE_BLOCKDEV]
        :raise: SocksTransmissionError if round-trip transmission failed.
        :raise: SocksInternalServerError if server returns an error.
        """

        results_s = self.send('blockdev')

        try:
            results = loads(results_s)
        except JSONDecodeError as exc:
            raise SocksTransmissionError('Could not decode data. Buffer size is possibly too small') from exc

        if results['status'] != 'Success':
            raise SocksInternalServerError(results['status'])

        devices = []

        for i in range(int(results['num_devices'])):
            device: complex_types.TYPE_BLOCKDEV = {
                'avail_blocks': int(results[f'available_blocks_{i}']),
                'avail_size': int(results[f'available_size_{i}']),
                'block_size': int(results[f'block_size_{i}']),
                'fstype': results[f'filesystem_type_{i}'],
                'host': results['host'],
                'mounted_device': results[f'mounted_device_{i}'],
                'mountpoint': results[f'mountpoint_{i}'],
                'name': results[f'name_{i}'],
                'path': results[f'path_{i}'],
                'total_blocks': int(results[f'total_blocks_{i}']),
                'total_size': int(results[f'total_size_{i}']),
            }
            devices.append(device)

        return devices

    def meminfo(self) -> complex_types.TYPE_MEMINFO:

        """Ask peer to list virtual memory.

        :return TYPE_MEMINFO
        :raise: SocksTransmissionError if round-trip transmission failed.
        :raise: SocksInternalServerError if server returns an error.
        """

        results_s = self.send('meminfo')

        try:
            results = loads(results_s)
        except JSONDecodeError as exc:
            raise SocksTransmissionError('Could not decode data. Buffer size is possibly too small') from exc

        if results['status'] != 'Success':
            raise SocksInternalServerError(results['status'])

        del results['status']

        results['totalram'] = int(results['totalram'])
        return results
