import http.server
import socketserver
import ssl 

def start_server(port: int, handler: http.server.SimpleHTTPRequestHandler, certificate: str, key: str):
    '''
    A sinple fu8nction that starts a https server

    :param port: the port the server should be started at
    :param handler: the request handler
    :param certificate: the path to the certificate.pem file
    '''
    with socketserver.TCPServer(("localhost", port), handler) as httpd:
        httpd.socket = ssl.wrap_socket (httpd.socket, certfile=certificate, keyfile=key, server_side=True, ssl_version=ssl.PROTOCOL_TLS)
        print(f'starting server at port: https://localhost:{port}')
        httpd.serve_forever()


PORT = 8080
handler = http.server.SimpleHTTPRequestHandler

start_server(PORT, handler, 'certificates/localhost.crt', 'certificates/localhost.key')
