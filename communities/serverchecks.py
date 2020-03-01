import requests
import socket
import time
import struct
import json

from requests.exceptions import RequestException, InvalidURL, Timeout
from json import JSONDecodeError

class ServerCheckFailed(Exception):
    def __init__(self, message, exc=None):
        self.message = message
        self.exception = exc

    def __str__(self):
        return self.message


def check_website(url):
    """Check if there is a valid website (GET returns response 200 with a HTML
    content type at the given URL.

    Raises ServerCheckFailed if not. 
    """
    r = _request_get(url)
    ct = r.headers['content-type']
    if not (ct.startswith("text/html") or ct.startswith("application/xhtml+xml")):
        raise ServerCheckFailed("Server did not return a HTML document")


def check_listserver(url):
    """Check that there is a Drawpile listserver at the given URL

    Raises ServerCheckFailed if not. 
    """
    r = _request_get(url)
    ct = r.headers['content-type']
    if not ct.startswith("application/json"):
        raise ServerCheckFailed("This does not seem to be a Drawpile list server (got wrong content type)")

    try:
        reply = r.json()
    except JSONDecodeError as e:
        raise ServerCheckFailed("This does not seem to be a Drawpile list server (could not parse returned JSON)", e)

    if reply.get('api_name') != 'drawpile-session-list':
        raise ServerCheckFailed("This is not a Drawpile list server")


def check_drawpile_server(address):
    """Check that there is a Drawpile server at the given address.

    The following address formats are supported:

    - domain
    - IPv4 address
    - address:port
    
    Raises ServerCheckFailed
    """
    port = 27750
    if ':' in address:
        address, port = address.split(':', 1)
        try:
            port = int(port)
        except ValueError:
            raise ServerCheckFailed("Not a port number: " + port)

    try:
        s = socket.create_connection((address, port), 5)
    except ConnectionRefusedError:
        raise ServerCheckFailed("Drawpile server does not appear to be running. (Server refused connection)")
    except OSError as e:
        raise ServerCheckFailed("Could not connect to the server", e)

    try:
        buf = b''
        start_time =time.time()
        payload_len = 0
        while True:
            b = s.recv(4096)
            if time.time() - start_time > 5:
                raise ServerCheckFailed("Timed out. Server responds too slowly.")
            if not b:
                raise ServerCheckFailed("This does not seem to be a Drawpile server. (Received unexpected data)")
            buf += b

            if payload_len == 0 and len(buf) > 4:
                payload_len, msg_type = struct.unpack('>HBx', buf[0:4])
                if msg_type != 0 or payload_len == 0 or payload_len > 0xffff:
                    raise ServerCheckFailed("This does not seem to be a Drawpile server.")

            if payload_len > 0 and len(buf) >= 4+payload_len:
                try:
                    response = json.loads(buf[4:4+payload_len])
                except JSONDecodeError as e:
                    raise ServerCheckFailed("This does not seem to be a Drawpile server.")

                if response.get('type') == 'login':
                    return # OK
                else:
                    raise ServerCheckFailed("This does not seem to be a Drawpile server.")

    except socket.timeout:
        raise ServerCheckFailed("This does not seem to be a Drawpile server.")
    finally:
        s.close()


def _request_get(url):
    try:
        r = requests.get(url, timeout=5)
    except InvalidURL as e:
        raise ServerCheckFailed("Invalid URL", e)
    except Timeout as e:
        raise ServerCheckFailed("Connection timed out", e)
    except RequestException as e:
        raise ServerCheckFailed("Could not connect to server", e)

    if r.status_code != 200:
        raise ServerCheckFailed(f"Server returned unexpexted status code ({r.status_code}). Expected 200 OK")

    return r


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: serverchecks.py <website|server|listserver> <url>")
        sys.exit(1)

    try:
        if sys.argv[1] == 'website':
            check_website(sys.argv[2])
        if sys.argv[1] == 'listserver':
            check_listserver(sys.argv[2])
        if sys.argv[1] == 'drawpile':
            check_drawpile_server(sys.argv[2])
        else:
            print("Unknown type:", sys.argv[1])
            sys.exit(1)

    except ServerCheckFailed as e:
        print("Server check failed:", e)
        if e.exception:
            print(type(e.exception), e.exception)
        sys.exit(2)
    else:
        print("Server check ok")

