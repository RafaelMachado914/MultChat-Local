import customtkinter as ctk



ctk.set_appearance_mode("dark")
chat = ctk.CTk()
chat.title("Chat")
chat.geometry("900x600")
chat.grid_columnconfigure(0, weight=1) 
chat.grid_columnconfigure(1, weight=3)
chat.grid_rowconfigure(0, weight=1)
chat.grid_rowconfigure(1, weight=0) 

lateral = ctk.CTkFrame(chat, corner_radius=0)
lateral.grid(row=0, column=0, sticky="nsew")



Ususario = ctk.CTkLabel(lateral, text="Usuário")
Ususario.pack(pady=10)

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


botao_entrar = ctk.CTkButton(lateral, text="Entrar")
botao_entrar.pack(pady=20)


Texto_chat = ctk.CTkTextbox(chat, width=500)
Texto_chat.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
Texto_chat.configure(state="disabled") 



Caixa_entrada = ctk.CTkFrame(chat, fg_color="transparent")
Caixa_entrada.grid(row=1, column=1, sticky="ew", padx=10, pady=10)


Caixa_entrada.grid_columnconfigure(0, weight=1)
Caixa_entrada.grid_columnconfigure(1, weight=0)

entrada_mensagem = ctk.CTkEntry(Caixa_entrada, placeholder_text="Digite...") 
entrada_mensagem.grid(row=0, column=0, sticky="ew", padx=(0, 10))

botao_enviar = ctk.CTkButton(Caixa_entrada, text="Enviar", width=80)
botao_enviar.grid(row=0, column=1)



chat.mainloop()