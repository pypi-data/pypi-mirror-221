from random import choice
from string import ascii_letters, digits, punctuation
from pytest import mark
from SocksDriver import SocksClient

ALPHANUMERIC = ascii_letters + digits

def generate_random_string(num_strings: int, len_strings: int) -> list[str]:
    result = []

    for _ in range(num_strings):
        result.append(''.join(choice(ALPHANUMERIC) for _ in range(len_strings)))

    return result

def generate_random_punctuation(num_strings: int, len_strings: int) -> list[str]:
    result = []

    for _ in range(num_strings):
        result.append(''.join(choice(punctuation) for _ in range(len_strings)))

    return result

# OS specific line break tests

def test_handle_line_feed(client: SocksClient) -> None:
    assert client.send('foobar\n') == 'foobar\n'

def test_handle_carriage_return(client: SocksClient) -> None:
    assert client.send('foobar\r') == 'foobar\r'

def test_handle_end_of_line(client: SocksClient) -> None:
    assert client.send('foobar\r\n') == 'foobar\r\n'

def test_handle_no_line_break(client: SocksClient) -> None:
    assert client.send('foobar') == 'foobar'

# Test "empty" messages
# Note that a true empty message, '', would be considered an EOF / hangup by the server

def test_handle_single_line_feed(client: SocksClient) -> None:
    assert client.send('\n') == '\n'

def test_handle_single_carriage_return(client: SocksClient) -> None:
    assert client.send('\r') == '\r'

def test_handle_single_end_of_line(client: SocksClient) -> None:
    assert client.send('\r\n') == '\r\n'

# Echo tests

@mark.parametrize('string', generate_random_string(num_strings=10, len_strings=15))
def test_echo_15_byte_string(client: SocksClient, string: str) -> None:
    assert string == client.send(string)

@mark.parametrize('string', generate_random_punctuation(num_strings=10, len_strings=15))
def test_echo_15_byte_punctuation(client: SocksClient, string: str) -> None:
    assert string == client.send(string)

@mark.skip(reason='Driver does not know how to handle buffer overflow')
def test_echo_max_size_minus_one_byte_string(client: SocksClient) -> None:

    string = generate_random_string(num_strings=1, len_strings=client.BUFFER_SIZE)
    assert string[0] == client.send(string[0])

@mark.skip(reason='Driver does not know how to handle buffer overflow')
def test_echo_max_size_plus_five_bytes_string(client: SocksClient) -> None:

    string = generate_random_string(num_strings=1, len_strings=client.BUFFER_SIZE + 5)
    first_chunk = string[0][0:1024]

    # What happens to string[0][1024:] data??
    # Gets left over in buffer and will screw up the next call
    # Any unit test placed in this file after this test will fail
    assert first_chunk == client.send(string[0])
