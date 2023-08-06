import json
import socket
from typing import Union


class RequestError(Exception):
    pass


class ServerError(Exception):
    pass


class CachierClient:
    def __init__(self: "CachierClient", host: str, port: str) -> None:
        self.host = host
        self.port = port
        self.sock = None

    def connect(self: "CachierClient") -> socket.socket:
        sock = socket.socket()
        sock.connect((self.host, self.port))

        self.sock = sock

        return self

    def get_server_response(self: "CachierClient") -> str:
        return self.sock.recv(1024).decode()

    def guard_invalid_connection(self: "CachierClient") -> None:
        if self.sock is None:
            raise ConnectionError("you must connect to the server first.")

    def guard_closed_connection(self: "CachierClient", data: str) -> None:
        if not data:
            raise ConnectionError("connection to the server is closed.")

    def guard_request_error(self: "CachierClient", data: str) -> None:
        status = data.get("status")
        if not status:
            raise ServerError(f"server returned invalid response {data}. please report this.")

        if status == "error":
            raise RequestError(data.get("message", "unknown error occurred. please report this."))

    def send(self: "CachierClient", message: str) -> None:
        self.guard_invalid_connection()

        if not isinstance(message, str):
            raise TypeError("message must be a string.")

        self.sock.send((message + "\n").encode())

    def get(self: "CachierClient", key: str) -> Union[str, None]:
        self.guard_invalid_connection()

        if not isinstance(key, str):
            raise TypeError("key must be a string.")

        request = {
            "command": "get",
            "key": key,
        }

        self.send(json.dumps(request))

        data = self.get_server_response()
        self.guard_closed_connection(data)

        serialized_data = json.loads(data)
        self.guard_request_error(serialized_data)

        # value can be empty string, so we need to check if it's present
        return serialized_data.get("value") or None

    def set(self: "CachierClient", key: str, value: str, ttl: Union[int, None]) -> None:
        self.guard_invalid_connection()

        if not isinstance(key, str):
            raise TypeError("Key must be a string.")

        if not isinstance(value, str):
            raise TypeError("Value must be a string.")

        if ttl is not None and not isinstance(ttl, int):
            raise TypeError("TTL must be an integer.")

        request = {
            "command": "set",
            "key": key,
            "value": value,
            "ttl": ttl,
        }

        self.send(json.dumps(request))

        data = self.get_server_response()
        self.guard_closed_connection(data)

        serialized_data = json.loads(data)
        self.guard_request_error(serialized_data)


def greetings():
    return "Hello, World!"


if __name__ == '__main__':
    client = CachierClient("localhost", 8080).connect()

    print("should be None:", client.get("greetings"))
    client.set("greetings", "Hello, World!", 10)
    print("should be something:", client.get("greetings"))
    import time
    time.sleep(11)
    print("should be None:", client.get("greetings"))
