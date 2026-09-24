import ssl
import socket


def connect(host: str, port: int):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    # Deliberately weak legacy configuration
    context.minimum_version = ssl.TLSVersion.TLSv1
    context.set_ciphers("AES128-SHA")

    sock = socket.create_connection((host, port))
    return context.wrap_socket(sock, server_hostname=host)