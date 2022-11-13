# Cliente socket #
## Trabalho de Conectividade de Sistemas CiberFísicos ##
### Gabriel Mocellin  &  Diogo Bonet ###

import socket 
#Códigos 7-12 explicados no código (serverSocket.py)
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!disc"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)














####    Funções utilizadas durante o programa!    ####
def enviar(msg):
    mensagem = msg.encode(FORMAT)
    msg_lenght = len(mensagem)
    enviar_lenght = str(msg_lenght).encode(FORMAT)
    enviar_lenght += b' ' * (HEADER - len(enviar_lenght))
    client.send(enviar_lenght)
    client.send(mensagem)


def definir_nickname():
    print('Qual será seu apelido no chat?\n')
    nickname = str(input('-> '))
    enviar(nickname)


def cliente():
    definir_nickname() #Antes do chat ser iniciado, o cliente deverá escolher um nome de exibição.

    print('\n\n\n[Chat iniciado!]')
    print('**Caso queira desconectar, digite: !disc**\n\n\n')
    while True:
        mensagem_cliente = str(input('> '))
        # data = client.recv(1024)
        #if(data):
        #    print(data)
        if(mensagem_cliente == '!disc'):
            return enviar(mensagem_cliente)
            break
        else:
            enviar(mensagem_cliente)











####    Iniciando programa!    ####
cliente()