# Servidor socket #
## Trabalho de Conectividade de Sistemas CiberFísicos ##
### Gabriel Mocellin  &  Diogo Bonet ###

import socket 
import threading

# Importando 'threading' para poder criar/usar vários clientes ao mesmo tempo.

HEADER = 64 #Quantidade de bytes que serão enviadas/recebidas durante as conversas entre cliente e servidor.
FORMAT = 'utf-8' #Formato usado para decodificação da mensagem do cliente.
DISCONNECT_MESSAGE = "!disc"

PORT = 5050
## SERVER = "cmd->ipconfig->IPV4" ***OU***
SERVER = socket.gethostbyname(socket.gethostname())
# Pega o IPV4 sozinho para utilizar no servidor.
### print(SERVER) Caso queira ver o IP sendo utilizado pelo servidor.
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TCP = Envia dados ao servidor em ordem (respeitando a ordem do envio) e recebe confirmação do envio/chegada ( SOCK_STREAM ).
# UDP = ( SOCK_DGRAM )
server.bind(ADDR)


clientes_conectados = {}




####    Funções utilizadas durante o programa!    ####
def handle_client(conn, addr):
    print(f'[Nova conexão] {addr} conectou-se!')

    nickname = setarNickname(conn, addr)

    connected = True
    while connected:
            msg = conn.recv(HEADER).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE: #Caso o usuário digite '!DISCONNECT' no chat, a conexão será finalizada.
                connected = False
            print(f'[{nickname}] {msg}')
    print(f'***   {nickname} DESCONECTOU-SE!   ***')
    return conn.close()


def setarNickname(conn, addr):
        msg = conn.recv(HEADER).decode(FORMAT)
        clientes_conectados[addr] = msg #Salvando em um dicionário o nome escolhido, para que, por meio do IP e PORTA o usuário possa ser identificado.
        print(f'\nO usuário {addr} está como: [{msg}]\n')
        return clientes_conectados[addr]


def startServer():
    server.listen() # O servidor irá "escutar" conexões de clientes.
    print(f"[Server está esperando conexões em {SERVER}]")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Conexões Ativas] {threading.active_count() - 1}")


def menuSocket():
    op = False
    while(op == False):
        print('======= Socket Menu v.1 =======\n')
        print('[1] | Iniciar Servidor')
        print('[0] | Sair' )
        print('\n======= Socket Menu v.1 =======\n')

        op = int(input('\nSelecione uma opção: '))

        if(op==1):
            print('\n\n\n[Iniciando servidor...]\n')
            return startServer()
        elif(op==0):
            return print('\n\n\nSaindo...')
        else:
            print(f'\n\n\nOpção [{op}] inválida! \nTente novamente!\n\n\n')
            op = False







####    Iniciando programa!    ####
menuSocket()