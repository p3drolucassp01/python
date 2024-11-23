m=[]
for i in range(4):
    #Preenchendo a matriz
  linha =[]
linha.append(input('Digite o nome da Pessoal ',str(i)+':'))
linha.append(int(input('Digite a idade de ',linha[0]+ ' : ')))
m.append(linha)

    #Procurando a pessoa mais nova
menor=m[0][1]
pos=0
for i in range(4):
 if m[i][1]<menor:
  menor=m[i][1]
pos=1
#Imprimir a Matriz
for i in range(4):
 print('A pessoa mais nova é', m[pos][0])

m = []
for i in range(4):
    # Preenchendo a matriz
    linha = []
    nome = input(f'Digite o nome da pessoa {i+1}: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    linha.append(nome)
    linha.append(idade)
    m.append(linha)

# Procurando a pessoa mais nova
menor = m[0][1]
pos = 0
for i in range(4):
    if m[i][1] < menor:
        menor = m[i][1]
        pos = i  # Corrigido para atualizar a posição da pessoa mais nova

# Imprimir a Matriz
for i in range(4):
    print(m[i])  # Corrigido para imprimir a linha inteira

print('A pessoa mais nova é', m[pos][0])