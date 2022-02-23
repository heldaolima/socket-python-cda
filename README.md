# Socket com CDA

Aplicação dos conceitos de socket em Python, usando poemas de Carlos Drummond de Andrade, para a disciplina de Redes de Computadores - UFAL 2022

## O que o programa faz
Há duas funcionalidades básicas, que funcionam no modelo cliente-servidor, capaz de responder a múltiplos clientes ao mesmo tempo:
- Disponibilização de 4 poemas de Carlos Drummond de Andrade, enviados ao cliente:
  - A Ingaia Ciência
  - Legado
  - Soneto da Loucura
  - Oficina Irritada
- Um pequeno jogo envolvendo esses poemas:
  - O usuário recebe um verso aleatório e deve dizer a qual dos 4 poemas o verso pertence
 
 ## Como executar
 1. Não há dependências a serem instaladas além do próprio Python
 2. Como o socket funciona com base no protocolo TCP, execute inicialmente o servidor (sempre dentro da pasta 'src', para não ter problemas com os arquivos):  
 ```
    cd src
    python3 server.py
 ```
 3. Em seguida, execute o cliente em outro terminal. Como é multithread, podem ser diversos clientes em diversos terminais:  
```
    cd src
    python3 client.py
```
4. No cliente, basta seguir os menus!
