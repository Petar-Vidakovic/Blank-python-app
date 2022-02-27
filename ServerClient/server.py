import socket
import threading

HDR = 64
port = 8989
SERVER = socket.gethostbyname(socket.gethostname())
addr = (SERVER, port)

fmt = 'utf-8'
dcMsg = "!DISCONNECT"
welcomeMsg = "Welcome to the server"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)


def handleClient(conn, addr):
    print(f"<New connection> {addr} connected.")

    connected = True
    while connected:
        msgLen = conn.recv(HDR).decode(fmt)
        if msgLen:
            msgLen = int(msgLen)
            msg = conn.recv(msgLen).decode(fmt)
            if msg == dcMsg:
                connected == False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(fmt))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] Server is starting...")
start()