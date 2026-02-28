import socket
import struct
import threading

ip_servidor = ''
porta = 5000

servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    servidor_udp.bind((ip_servidor, porta))
except:
    print("Erro, tente novamente")

usuario = ''

def receber_mensagens(servidor_udp):
   while True:
       try:
           mensagem = servidor_udp.recv(2048).decode('utf-8')
           print(mensagem + '\n') 
       except:
           print('Desconectado')
           servidor_udp.close()
           break

def enviar_mensagens(servidor_udp, usuario):
     while True:
        try:
            mensagem = input('\n')
            servidor_udp.sendto('<{usuario}>: {mensagem}'.encode('utf-8'), (ip_servidor, porta))
        except:
            return

Recebendo = threading.Thread(target=receber_mensagens, args=[servidor_udp])
Enviando = threading.Thread(target=enviar_mensagens, args=[servidor_udp, usuario])

Recebendo.start()
Enviando.start()
