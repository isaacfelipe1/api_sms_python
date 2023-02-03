from tkinter import *
from tkinter import messagebox
from telesign.messaging import MessagingClient
def Enviar_sms():
    identificacao_cliente ="DA9CE9DF-13D6-4A40-B311-BEDA13895522"
    chave_api = "2ILYkJE3aovlKzIzDiVwck6CgJ/QEpC8pWB55CJ847zn9oNPSV2pn76GKYO47gZOwSMaowdMNpT9RY13d3OGwg=="
    numero_telefone = "55" + txt_numero.get()
    mensagem= txt_mensagens.get()
    tipo_de_mensagem = "ARN"
    mensagens = MessagingClient(identificacao_cliente, chave_api)
    resposta = mensagens.message(numero_telefone, mensagem, tipo_de_mensagem)
    if resposta.status_code == 200:
        messagebox.showinfo("SMS Enviado Com Sucesso")
    else:
        messagebox.showerror("Falha ao enviar SMS")

principal = Tk()
principal.title('SMS Envio Python')
principal.geometry('200x200')

linhas = 0
while linhas < 20:
    principal.rowconfigure(linhas, weight=1)
    principal.columnconfigure(linhas, weight=1)
    linhas += 1

txt_numero = Entry(principal)
txt_numero.insert(0, 'Digite seu Numero')
txt_numero.grid(row=1, column=5, sticky='NS')

txt_mensagens = Entry(principal)
txt_mensagens.insert(0, 'Digite sua Mensagem')
txt_mensagens.grid(row=3, column=5, sticky='NS')

btn_enviar = Button(principal, text='Enviar',command=Enviar_sms)
btn_enviar.grid(row=5, column=5, sticky='NESW')
principal.mainloop()
