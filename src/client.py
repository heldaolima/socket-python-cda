import socket

HEADER = 2048
PORT = 1234
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) #string -> bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))


print(client.recv(HEADER).decode(FORMAT))
mensagem = ""
while mensagem != DISCONNECT_MESSAGE:
    mensagem = str(input("\nInsira a mensagem: "))
    send(mensagem)
