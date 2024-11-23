'''Atividade 1'''
'''
mercadoria = str (input('Informe o nome da mercadoria: '))
mercadoria1 = float (input('Informe o valor: '))
mercadoria2 = float (input('informe o percentual de desconto: '))
desconto = mercadoria1 *(1-(mercadoria2/100))
print('O valor da mercadoria',mercadoria, 'sera de',mercadoria2,'%','e ficara no valor final de', desconto)
'''

'''Atividade 2'''
'''
distancia = float(input("Digite a distância em km: "))

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print("Preço da passagem:", preço)
'''

'''Atividade 3'''
'''
valor_inicial = float(input("Digite o valor inicial depositado: R$ "))
valor_mensal = float(input("Digite o valor a ser depositado mensalmente: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (%): ")) / 100
meses = int(input("Digite o número de meses: "))


saldo = valor_inicial

for mes in range(1, meses + 1):
    saldo += valor_mensal 
    saldo += saldo * taxa_juros  
    print(f"Saldo após o mês {mes}: R$ {saldo:.2f}")

print(f"\nSaldo final após {meses} meses: R$ {saldo:.2f}")

'''

'''Atividade 4'''
'''
cidades = ['Recife', 'Olinda', 'Paulista']


for i in range(3):
    cidade = input(f"Digite o nome da cidade {i + 1}: ")
    cidades.append(cidade)  


print("\nLista de cidades:")
for cidade in cidades:
    print(cidade)

'''

'''Atividade 5'''
'''
numeros = [15, 28, 46, 58, 59, 82, 89, 99, 100]

numero_usuario = int(input("Digite um número para verificar se está na lista: "))

if numero_usuario in numeros:
    print(f"O número {numero_usuario} está na lista.")
else:
    print(f"O número {numero_usuario} não está na lista.")
'''
 
'''Atividade 6''' 
  
'''
def calcular_imc(altura, peso):
    
    imc = peso / (altura ** 2)
    
    # Exibir o IMC
    print(f"Seu IMC é: {imc:.2f}")
    
    # Classificação com base no IMC
    if imc < 18.5:
        print("\nSua classificação é Magreza")
    elif 18.5 <= imc < 24.9:
        print("\nSua classificação é Saudável")
    elif 25 <= imc < 29.9:
        print("\nSua classificação é Sobrepeso")
    elif 30 <= imc < 34.9:
        print("\nObesidade Grau I")
    elif 35 <= imc < 39.9:
        print("\nObesidade Grau II (mórbida)")
    else:
        print("\nObesidade Grau III (mórbida)")


altura = float(input('Digite sua altura (em metros): ')) 

peso = float(input('Digite seu peso (em kg): '))

calcular_imc(altura, peso)
'''
     
