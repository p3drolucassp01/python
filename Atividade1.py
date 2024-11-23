'''acesso = 'Global'

def mudarAcesso():
    acesso='Local'
    print('Acesso anterior da função:', acesso)

mudarAcesso()
print('Acesso no exterior da função:', acesso)'''

'''def lin():
    print('-'*30)
lin()
print('         Python     ')
lin()
print('         Curso     ')
lin()
print('         Funções     ')
lin()'''

'''
def cadastrar(nome, idade, mensagem='Dados com sucesso'):
    print(nome,'Possui a idade de ',idade, 'anos')
    print(mensagem)
cadastrar('Pedro', 19, 'Parabens')
'''
'''
def validarsenha(senha):
    if len(senha)<8:
        return False
    elif not any(char.isdigit() for char in senha):
        return False
    elif not any(char.isalpha() for char in senha):
        return False
    else:
        return True
senha="abc123"
resultado=validarsenha(senha)
print(resultado)
'''

'''def imc():

 altura = float (input('digite sua altura: '))
 peso = float (input('digite seu peso: '))

 imc = float
 imc=peso/(altura**2)
 print("Seu IMC é: ", imc)
    
 if (imc < 18.5):
  print("\nSua classificação é Magreza")

 elif 18.5 <=imc < 24.9: 
  print("\nSua classificação é Saudável")

 elif 25 <= imc < 29.9:
  print("\nOSua classificação é Sobrepeso")

 elif 30 <= imc < 34.9:
  print("\nObesidade Grau I")

 elif 35 <= imc  < 39.9:
  print("\nObesidade Grau II (mórbida)")
 
 else: 
  print("\nObesidade Grau III (mórbida)")
 
 
imc()'''
'''
def somadiv(V1=1,V2=10):
 somadivi = V1 + V2/2

somadiv()
'''










