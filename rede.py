import socket
import struct
import threading
import json
from datetime import datetime

ip_grupo = '224.1.1.1'
porta = 5000

servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

try:
    servidor_udp.bind(('', porta))

except:
    print("Erro, tente novamente")


enpacotar = struct.pack("4sl", socket.inet_aton(ip_grupo), socket.INADDR_ANY)
servidor_udp.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, enpacotar)

usuario = 'usuario'

recebida = ''

def receber_mensagens(servidor_udp):
   while True:
       try:
           dados, mensagem = servidor_udp.recv(2048)
           mensagem_convertida = json.loads(dados.decode('utf-8'))
           recebida = mensagem_convertida
           return recebida
       except:
           servidor_udp.close()
           break



Recebendo = threading.Thread(target=receber_mensagens, args=[servidor_udp])
Enviando = threading.Thread(target=enviar_mensagens, args=[servidor_udp,usuario])


Recebendo.start()
Enviando.start()
