from tkinter import *
from tkinter import ttk
root=Tk()

class Application():
    def __init__(self):
        self.root=root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="blue")
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=988,height=788)
        self.root.minsize(width=488,height=388)

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg="#CCCCCC",
                            highlightbackground="#FFCC99", highlightcolor="#FF66CC")
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg="#CCCCCC",
                            highlightbackground="#CC0066", highlightcolor="#FF66FF")
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        
    def criando_botoes(self):
        self.bt_limpar = Button(self.frame1, text="limpar")
        self.bt_limpar.place(relx=0.6, rely= 0.1, relheight=0.15)
        #criaçao botao buscar
        self.bt_limpar = Button(self.frame1, text="buscar")
        self.bt_limpar.place(relx=0.5, rely= 0.1, relheight=0.15)
        #criaçao do botao novo
        self.bt_limpar = Button(self.frame1, text="novo")
        self.bt_limpar.place(relx=0.4, rely= 0.1, relheight=0.15)
        #criaçao do botao alterar
        self.bt_limpar = Button(self.frame1, text="altera")
        self.bt_limpar.place(relx=0.3, rely=0.1, relheight=0.15)
        #craiçao do botao apagar
        self.bt_limpar = Button(self.frame1, text="apagar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relheight=0.15)
        
        #criação label
        
        self.lb_codigo=Label(self.frame1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05, relheight=0.05)
        
        self.codigo_entry=Entry(self.frame1)
        self.codigo_entry.place(relx=0.05, rely=0.15,relwidth=0.08)
        
        #ciração de lebel de entrada de nome
        self.lb_nome=Label(self.frame1, text="Nome")
        self.lb_nome.place(relx=0.05,rely=0.35)
        
        self.nome_entry=Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.15,relwidth=0.08)
        
        #ciração de lebel de entrada de telefone
        self.lb_nome=Label(self.frame1, text="telefone") 
        self.lb_nome.place(relx=0.05,rely=0.36)
        self.nome_entry=Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.7,relwidth=0.8)
        
 


Application()