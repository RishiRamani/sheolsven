import ssl
import socket


def connect(host: str, port: int):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

    context.minimum_version = ssl.TLSVersion.TLSv1_3
    context.maximum_version = ssl.TLSVersion.TLSv1_3

    context.load_default_certs()

    sock = socket.create_connection((host, port))

    return context.wrap_socket(
        sock,
        server_hostname=host
    )