import os
import socket
import ssl
from waitress import serve
from core.wsgi import application  

if __name__ == '__main__':
    print("Elektron kassa açyk! Serwer HTTPS (port 443) bilen işleýä...")
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 443))
    server_socket.listen(1024)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(
        certfile=os.path.join(BASE_DIR, 'marytelecomkassa.tm.crt'), 
        keyfile=os.path.join(BASE_DIR, 'marytelecomkassa.tm.key')
    )
    
    secure_socket = context.wrap_socket(server_socket, server_side=True)

    serve(application, sockets=[secure_socket])