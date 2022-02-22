import socket 
import threading
from random import randint

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
    boas_vindas = """4 Poemas de Carlos Drummond de Andrade e um joguinho
Para ler os poemas, insira '1' ou 'poemas'
Para jogar, insira '2' ou 'jogo'
Para desconectar, envie '!DISCONNECT'"""
    conn.send(boas_vindas.encode(FORMAT))

    connected = True
    flag_jogo = False
    flag_poemas = False
    primeira = True
    num = 0

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #tamanho da msg
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) #msg ipsa
            
            print(f"[{addr}] {msg}")
            
            if msg == DISCONNECT_MESSAGE:
                conn.send("Desconectando...".encode(FORMAT))
                connected = False
                break
            
            elif primeira:
                if msg.lower() == 'jogo' or msg == '2':
                    primeira = False
                    flag_jogo = True
                    num = randint(1, 4) #escolher um poema aleatório
                    file_name = ''

                    if num == 1: 
                        file_name = 'conteudo/ingaia.txt'
                    elif num == 2:
                        file_name = 'conteudo/legado.txt'
                    elif num == 3:
                        file_name = 'conteudo/loucura.txt'
                    elif num == 4:
                        file_name = 'conteudo/oficina.txt'
                    
                    verso = ''

                    arquivo = open(file_name, 'r')

                    conteudo = arquivo.readlines()
                    
                    linha = randint(1, len(conteudo)-1) #escolher um verso aleatório do poema
                    while conteudo[linha] == '\n': #que não pode ser uma linha vazia
                        linha = randint(1, len(conteudo)-1)
                    
                    verso = conteudo[linha] 
                    arquivo.close()

                    desafio = f"""Iniciando o jogo...
    -- Regras do jogo:
        - Você receberá um verso de um dos poemas 
        - Basta dizer a qual poema pertence o verso 
        - Você vence se a reposta estiver correta
    
    Verso: {verso}
    * Se você acha que é 'A Ingaia Ciência', insira 1
    * Se você acha que é 'Legado', insira 2
    * Se você acha que é 'Soneto da Loucura', insira 3
    * Se você acha que é 'Oficina Irritada', insira 4
    * Se você quiser desconectar, envie '!DISCONNECT'"""

                    conn.send(desafio.encode(FORMAT))

                elif msg.lower() == 'poemas' or msg == '1':
                    primeira = False
                    flag_poemas = True
                    menu = """Carregando poemas...\n4 Poemas de Carlos Drummond de Andrade
    [1] A Ingaia Ciência
    [2] Legado
    [3] Soneto da Loucura
    [4] Oficina Irritada
    
    Para desconectar, envie '!DISCONNECT' """
                    conn.send(menu.encode(FORMAT))
                else:
                    conn.send("Mensagem inválida recebida! Tente de novo.".encode(FORMAT))

            else:
                if flag_jogo:
                    if msg.isnumeric() and int(msg) == num:
                        result = "Correto! Vejo que você é um especialista na poesia de Drummond!\n\n"
                        
                    else:
                        result = "Incorreto! Mas você pode tentar novamente!\n\n"
                    flag_jogo = False
                    primeira = True

                    conn.send((result+boas_vindas).encode(FORMAT))

                elif flag_poemas:
                    if msg in ["1", "2", "3", "4"]:        
                        if msg == "1":
                            arquivo = open('conteudo/ingaia.txt', 'r')
                            conn.send(arquivo.read().encode(FORMAT))
                            arquivo.close()
                        elif msg == "2":
                            arquivo = open('conteudo/legado.txt', 'r')
                            conn.send(arquivo.read().encode(FORMAT))
                            arquivo.close()
                        elif msg == "3":
                            arquivo = open('conteudo/loucura.txt', 'r')
                            conn.send(arquivo.read().encode(FORMAT))
                            arquivo.close()
                        elif msg == "4":
                            arquivo = open('conteudo/oficina.txt', 'r')
                            conn.send(arquivo.read().encode(FORMAT))
                            arquivo.close()
                    else:
                        conn.send("Mensagem inválida recebida! Tente de novo.".encode(FORMAT))
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