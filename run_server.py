import socket
import ssl
from waitress import serve
from core.wsgi import application  

if __name__ == '__main__':
    print("Elektron kassa açyk! Serwer HTTPS (port 443) bilen işleýä...")
    
    # 1. Создаем сетевой сокет и привязываем к порту 443
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 443))
    server_socket.listen(1024)

    # 2. Настраиваем SSL-контекст с сертификатами
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(
        certfile='marytelecomkassa.tm.crt', 
        keyfile='marytelecomkassa.tm.key'
    )
    
    # 3. Оборачиваем сокет в SSL
    secure_socket = context.wrap_socket(server_socket, server_side=True)

    # 4. ВАЖНО: В serve передаем ТОЛЬКО application и sockets!
    # Не добавляйте сюда cert_file, key_file, port или host!
    serve(application, sockets=[secure_socket])