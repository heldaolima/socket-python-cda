import socket 
import threading

HEADER = 2048 #tamanho de bits
PORT = 1234 #porta que não está sendo usada
SERVER = socket.gethostbyname(socket.gethostname()) # roda em qualquer pc
ADDR = (SERVER, PORT) #endereço
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(FAMILIA, TIPO)
server.bind(ADDR) #bind o socket nesse endereço

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    boas_vindas = """4 Poemas de Carlos Drummond de Andrade
    [1] A Ingaia Ciência
    [2] Legado
    [3] Memória
    [4] Oficina Irritada
    
    Para desconectar, envie '!DISCONNECT' """
    conn.send(boas_vindas.encode(FORMAT))

    connected = True
    # primeira = False
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #tamanho da msg
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) #msg ipsa
            
            print(f"[{addr}] {msg}")
            
            if msg == "1":
                arquivo = open('conteudo/ingaia.txt', 'r')
                conn.send(arquivo.read().encode(FORMAT))
                arquivo.close()
            elif msg == "2":
                arquivo = open('conteudo/legado.txt', 'r')
                conn.send(arquivo.read().encode(FORMAT))
                arquivo.close()
            elif msg == "3":
                arquivo = open('conteudo/memoria.txt', 'r')
                conn.send(arquivo.read().encode(FORMAT))
                arquivo.close()
            elif msg == "4":
                arquivo = open('conteudo/oficina.txt', 'r')
                conn.send(arquivo.read().encode(FORMAT))
                arquivo.close()
            elif msg == DISCONNECT_MESSAGE:
                conn.send("Desconectando...".encode(FORMAT))
                connected = False
            else:
                conn.send("Mensagem inválida recebida".encode(FORMAT))
    conn.close()


def start(): # novas coneexões
    server.listen()
    print(f"[Listening] O servidor está ouvindo em [{SERVER}]")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}"  )


print("[INICIANDO] O servidor está iniciando")
start();