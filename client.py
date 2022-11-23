# Cliente socket #
## Trabalho de Conectividade de Sistemas CiberFísicos ##
### Gabriel Mocellin  &  Diogo Bonet ###



import socket 
import threading



#Códigos 7-12 explicados no código (serverSocket.py)
HEADER = 64
PORT = 9999
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!disc"
SERVER = "26.28.22.163"
ADDR = (SERVER, PORT)



####    Funções utilizadas durante o programa!    ####
def enviar():
    while True:
        mensagem_cliente = str(input(''))
        if(mensagem_cliente == '!disc'):
            mensagem = mensagem_cliente.encode(FORMAT) # Codificação da mensagem enviada.

            return client.send(mensagem)
        else:
            mensagem = mensagem_cliente.encode(FORMAT)
            client.send(mensagem)


def receber():
    while True:
        data = client.recv(HEADER).decode(FORMAT) # Descodificação da mensagem recebida.
        print(data)


def definir_nickname():
    print('Qual será seu apelido no chat?\n')
    nickname = str(input('-> '))
    nickname = nickname.encode(FORMAT)
    return client.send(nickname)


def cliente():
    definir_nickname() #Antes do chat ser iniciado, o cliente deverá escolher um nome de exibição.

    print('\n\n\n[Chat iniciado!]')
    print('**Caso queira desconectar, digite: !disc**\n\n\n')

    thread1.start()
    thread2.start()



####    Criando Threading's    ####
thread1 = threading.Thread(target=enviar, args=())
thread2 = threading.Thread(target=receber, args=())



####    Iniciando programa!    ####
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except:
    print('\n\n\n[Conexão falhou!] Revise o IP e a PORTA e tente novamente...')
cliente()