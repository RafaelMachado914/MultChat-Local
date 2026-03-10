import customtkinter as ctk
import rede
import json
from datetime import datetime




ctk.set_appearance_mode("dark")
chat = ctk.CTk()
chat.geometry("900x600")
chat.grid_columnconfigure(0, weight=1) 
chat.grid_columnconfigure(1, weight=3)
chat.grid_rowconfigure(0, weight=1)
lateral = ctk.CTkFrame(chat, corner_radius=0)
lateral.grid(row=0, column=0, sticky="nsew")


LabelUsusario = ctk.CTkLabel(lateral, text="Usuário")
LabelUsusario.pack(pady=10)
Entrada_usuario = ctk.CTkEntry(lateral, placeholder_text="Usuario")
Entrada_usuario.pack(pady=5)

IP_Conversa = ctk.CTkLabel(lateral, text="IP da conversa")
IP_Conversa.pack(pady=5)
Entrada_ip = ctk.CTkEntry(lateral, placeholder_text="IP")
Entrada_ip.pack(pady=5)

Porta = ctk.CTkLabel(lateral, text="Selecione a porta")
Porta.pack(pady=5)
Porta_selecionada = ctk.CTkEntry(lateral, placeholder_text="Porta")
Porta_selecionada.pack(pady=5)

Texto_chat = ctk.CTkTextbox(chat, width=500)
Texto_chat.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
Texto_chat.configure(state="disabled") 

Caixa_entrada = ctk.CTkFrame(chat, fg_color="transparent")
Caixa_entrada.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
Caixa_entrada.grid_columnconfigure(0, weight=1)
Caixa_entrada.grid_columnconfigure(1, weight=0)
entrada_mensagem = ctk.CTkEntry(Caixa_entrada, placeholder_text="Digite...") 
entrada_mensagem.grid(row=0, column=0, sticky="ew", padx=(0, 10))


def enviar():
    texto = entrada_mensagem.get()
    rede.ip_grupo = Entrada_ip.get()
    rede.porta = int(Porta_selecionada.get())
    rede.servidor_udp.sendto(
        json.dumps({
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "username": rede.usuario,
            "message": texto
        }).encode("utf-8"),(rede.ip_grupo, rede.porta) )
    print(f"Enviado: {texto}")
    entrada_mensagem.delete(0, "end")

def mostrar_mensagem(msg):
    Texto_chat.configure(state="normal")

    Texto_chat.insert("end",f"\n{msg['date']} {msg['time']}\n{msg['username']}: {msg['message']}\n" )
    print(msg)
    Texto_chat.configure(state="disabled")
    Texto_chat.see("end")

def entrar():
    rede.usuario = Entrada_usuario.get()
    rede.recebida = mostrar_mensagem
    rede.iniciar(Entrada_ip.get(), int(Porta_selecionada.get()))
    botao_enviar.configure(state="normal")

botao_entrar = ctk.CTkButton(lateral, text="Entrar",command=entrar)
botao_entrar.pack(pady=20)


def sair():
    rede.ip_grupo = None
    rede.porta = None
    rede.servidor_udp.close()
    chat.destroy()

botao_sair = ctk.CTkButton(lateral, text="Sair",command=sair)
botao_sair.pack(pady=20)

botao_enviar = ctk.CTkButton(Caixa_entrada, text="Enviar", width=80, command=enviar)
botao_enviar.grid(row=0, column=1)
botao_enviar.configure(state="disabled")

if __name__ == "__main__":
    chat.mainloop()
