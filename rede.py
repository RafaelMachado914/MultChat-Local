import socket
import struct
import multiprocessing
import json
from datetime import datetime

ip_grupo = None
porta = None
servidor_udp = None
usuario = None
recebida = None


def iniciar(ip, port):
    global ip_grupo, porta, servidor_udp, usuario, recebida
    ip_grupo = ip
    porta = port
    servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    servidor_udp.bind(('', porta))

    enpacotar = struct.pack("4s4s", socket.inet_aton(ip_grupo), socket.INADDR_ANY,socket.inet_aton("0.0.0.0"))
    servidor_udp.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, enpacotar)

    Recebendo = multiprocessing.Process(target=receber_mensagens,args=(servidor_udp,),daemon=True)
    Recebendo.start()

def receber_mensagens(servidor_udp):
   while True:
       try:

           data, addr = servidor_udp.recvfrom(2048)
           mensagem_convertida = json.loads(data.decode('utf-8'))


           if recebida:
                recebida(mensagem_convertida)
       except:
           servidor_udp.close()
           break
       



