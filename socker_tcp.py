from socket import *
from multiprocessing import Process
import sys

HOST = "127.0.0.1"
PORT = 26029

def server_start():
    """
    lancement d'une socker en mode server
    """
    # AF_INET: socket réseau != AF_UNIX (///path/to/file.sock)
    # SOCK_STREAM: scoker tcp != SOCK_DGRAM udp
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)
        return server
    except ConnectionError as e:
        return e


def server_accept(server):
    """
    gestion des connexions serveur
    """
    sock, addr = server.accept()
    with sock:
        while True:
            # récéption jusqu'à 1024 octets
            s_data = sock.recv(1024)    
            if s_data != b'':
                _str = s_data.decode("utf8")
                print(f"server received : {_str}")
                sock.sendall(bytes(_str[::-1], "utf8"))
            if s_data == b"quit":
                sys.exit(0)
            




if __name__ == "__main__":
    server = server_start()
    p = Process(target=server_accept, args=(server,))
    p.start()

    with socket(AF_INET, SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(b'nouveau message')
        response = client.recv(1024)
        print(f"réponse: {response.decode('utf8')}")
        client.sendall(b"quit")
        server.close()

