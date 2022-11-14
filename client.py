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

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except:
    print('\n\n\n[Conexão falhou!] Revise o IP e a PORTA e tente novamente...')














####    Funções utilizadas durante o programa!    ####
def enviar(msg):
    mensagem = msg.encode(FORMAT)
    return client.send(mensagem)


def definir_nickname():
    print('Qual será seu apelido no chat?\n')
    nickname = str(input('-> '))
    return enviar(nickname)


def cliente():
    definir_nickname() #Antes do chat ser iniciado, o cliente deverá escolher um nome de exibição.

    print('\n\n\n[Chat iniciado!]')
    print('**Caso queira desconectar, digite: !disc**\n\n\n')
    while True:
        mensagem_cliente = str(input('> '))
        if(mensagem_cliente == '!disc'):
            return enviar(mensagem_cliente)
            break
        else:
            enviar(mensagem_cliente)











####    Iniciando programa!    ####
cliente()