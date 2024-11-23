'''
Al Pedro lucas de souza pessoa
19/09/2024

exercicio 1

velocidade = int(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
    
    excesso = velocidade - 80
    multa = excesso * 5
    print(f"Você foi multado! O valor da multa é R$ {multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade.")
'''

'''
exercicio 2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
'''
'''
exercico 3
valor_casa = int(input("Digite o valor da casa: R$ "))
salario = int(input("Digite o seu salário: R$ "))
anos = int(input("Digite a quantidade de anos para pagar: "))

meses = anos * 12
prestacao_mensal = valor_casa // meses

limite_prestacao = salario * 30 // 100 

if prestacao_mensal <= limite_prestacao:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R$ {prestacao_mensal}")
else:
    print("Empréstimo negado!")
    print(f"Valor da prestação mensal: R$ {prestacao_mensal} excede o limite de 30% do seu salário (R$ {limite_prestacao}).")
    '''
'''
exercicio 4
pessoa = {
    "nome": "Pedro",
    "idade": 21,
    "cidade": "Camaragibe"
}

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']} anos")
print(f"Cidade: {pessoa['cidade']}")
'''
'''
exercico 5

for i in range (4, -1, -1):
    print(i)
'''

'''
exercicico 6

idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))
    
    idades.append(idade)
    alturas.append(altura)

print("\nIdades e Alturas na ordem inversa:")
for i in range(4, -1, -1):
    print(f"Pessoa {i + 1}: Idade: {idades[i]}, Altura: {alturas[i]:.2f} m")
'''
'''
exercicio 7

class Clientes:
    def __init__(self, nomec, sobrenomec, cpfc, rendac):
        self.nomec=nomec
        self.sobrenomec=sobrenomec
        self.cpfc=cpfc
        self.rendac=rendac

    def mostraClientes(self):
          print('      Clientes         ')
          print('-----------------------')
          print(f'Nome: {self.nomec}')
          print('-----------------------')
          print(f'Sobrenome: {self.sobrenomec}')
          print('-----------------------')
          print(f'CPF: {self.cpfc}')
          print('-----------------------')
          print(f'Renda: {self.rendac}')






class Funcionarios:
    def __init__(self, nomef, sobrenomef, cpff, matriculaf):
        self.nomef=nomef
        self.sobrenomef=sobrenomef
        self.cpff=cpff
        self.matriculaf=matriculaf

    def mostraFuncionarios(self):
            print('Funcionarios: ')
            print('-----------------------')
            print(f'Nome: {self.nomef}')
            print('-----------------------')
            print(f'Sobrenome: {self.sobrenomef}')
            print('-----------------------')
            print(f'CPF: {self.cpff}')
            print('-----------------------')

            print(f'Matricula: {self.matriculaf}')

    

    


cliente1=Clientes('Lucas', 'Pessoa', '10063367459', 1500)
cliente2=Clientes('ryan', 'Lucas', '10068949521', 4000)
cliente3=Clientes('angelo', 'caro', '24463359412', 3500)

Funcionario1=Funcionarios('pedro', 'lucas', '49924524312', '102422533')
Funcionario2=Funcionarios('kayo', 'fernando', '49894524312', '112429856')
Funcionario3=Funcionarios('Jose', 'agnaldo', '49076524312', '187654533')

cliente1.mostraClientes()
cliente2.mostraClientes()
cliente3.mostraClientes()

Funcionario1.mostraFuncionarios()
Funcionario2.mostraFuncionarios()
Funcionario3.mostraFuncionarios()      
'''