#command while

'''i=1
while i < 10:
    print(i)
    i = i + 1
    print("contando..")'''

'''linguagem=""
while linguagem !="python":
    print('Qual linguagem estamos estudando? ')
    linguagem=input()
    print('Parabens! Você acertou!')'''

'''texto="\n Digite 'sair' para encerrar o programa"
texto +="\n Digite alguma mensagem: "
mensagem=""

while mensagem != 'sair':
    mensagem=input(texto)
print(mensagem)'''

'''i=0
while i <= 30:
    print(i)
    i += 5
    print("loading..")'''
    
#ranking top 3
'''ranking = ['joao','maria','igor','paulo','laura','andre','alex']

print('top 3: ')
for nome in ranking[:3]:
    print('\t' +  nome)
    

    print('lista 3: ')
    for nome in ranking[-3:]:
        print('\n' + nome)
'''
cores = ['preto', 'Azul', 'amarelo', 'rosa']
cores.sort()

for i, cor in enumerate(cores, start= 0):
    print(f"{i + 1}. {cor}")
    