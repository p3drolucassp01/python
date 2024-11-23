'''from tkinter import *
import tkinter as tk

janela=Tk()
janela.title('App SSystem')
janela['bg']='yellow'
#janela.minsize(300,100)
#janela.maxsize(600,300)
janela.geometry('300x200+550+150')
'''
'''
nome_title=tk.Label(janela, text='Trabalhando com bordas',bg='#FFFF00', height=2, width=35, relief= 'groove', fg='black', font=('Verdana', 20, 'bold'))
nome_title.place(x=100, y=20)
'''
'''
botao=tk.Button(janela, text='Entrar',bg='red', font=('Arial', 25))
botao.place(x=100, y=20)
botao1=tk.Button(janela, text='Enviar',bg='red', font=('Arial', 25))
botao1.place(x=300, y=20)

mainloop()
'''
import tkinter as tk

# Create the main window
janela = tk.Tk()
janela.title('App System')
janela['bg'] = 'blue'
janela.geometry('300x200+150+100')

# Uncomment and use the title label if needed
# nome_title = tk.Label(janela, text='Trabalhando com Bordas', bg='blue', height=2, width=35, relief='groove', fg='black', font=('Verdana', 20, 'bold'))
# nome_title.pack(pady=10)

# Uncomment and use buttons if needed
# botao = tk.Button(janela, text='Entrar', bg='red', font=('Arial', 25))
# botao.place(x=100, y=20)
# botao1 = tk.Button(janela, text='Enviar', bg='red', font=('Arial', 25))
# botao1.place(x=100, y=80)

# Creating labels with different border styles
nome1 = tk.Label(janela, text='Borda Groove', relief='groove')
nome1.place(x=20, y=20)

nome2 = tk.Label(janela, text='Borda Flat', relief='flat')
nome2.place(x=20, y=50)

nome3 = tk.Label(janela, text='Borda Raised', relief='raised')
nome3.place(x=20, y=80)

nome4 = tk.Label(janela, text='Borda Sunken', relief='sunken')
nome4.place(x=20, y=110)

nome5 = tk.Label(janela, text='Borda Ridge', relief='ridge')
nome5.place(x=20, y=140)

# Entry fields
entrada1 = tk.Entry(janela)  # Default width
entrada1.pack(pady=5)

entrada2 = tk.Entry(janela, width=30)  # Width of 30
entrada2.pack(pady=5)

# Start the Tkinter main loop
janela.mainloop()