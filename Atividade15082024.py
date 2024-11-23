#trabalhando com strings

'''
valor=input('Digite uma palavra: ')
print('O tipo primitivo é: ', type(valor))#tipo primitivo
print('Tem Espaço ?', valor.isspace())#Tem espaço 
print('É um numero ?', valor.isnumeric())# É numerico
print('É alfabetico ?', valor.isalpha())# é alfabetico
print('É alfanumerico ?', valor.isalnum())#é alfanumerico
print('está em maiuscula ?', valor.isupper())# é maiuscula
print('está em minuscula ?', valor.islower())#é minuscula 
print('a primeira letra é maiuscula ?', valor.istitle())# a primeira letra é maiuscula
'''
'''
texto ='pedrolucas.com'
print(texto[3])

texto ='pedrolucas.com'
print(texto[3:9])
'''
'''
import random


numero_aleatorio = random.randint(0, 100)


print("Número aleatório gerado:", numero_aleatorio)
'''

'''
texto = 'wqgourwdhsgisdfd@ogf89pwe.com'
print('@')'''

'''
texto = 'wqdgourhsgisdfd@ogf89pwe.com'
posicao = (texto.find('@'))
print(texto[posicao+0])
''' 
'''
idade = int(input('Digite sua idade: '))
if idade >= 18:{
    print('Você é maior de idade')

}
else:{
    print('Você é menor de idade')
}
    '''
'''
salario = int(input('Digite seu salário: '))
if salario >= 5000:{
    print('Você terá um aumento de 10%, valor total',(salario*0.10)+salario)

}
else:{
    print('Você terá um aumento de 5%, Valor total', (salario*0.05)+salario)
}
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

if n1 == n2:{
    print(f'Número {n1} é igual ao {n2}')
}

else:{
    print(f'Número{n1} é Diferente ao {n2}')
}