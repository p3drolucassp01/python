# matriz
'''
notas = [
    [7.5, 8.0, 6.5, 9.0, 10.0],  # Notas do primeiro aluno
    [5.0, 6.5, 7.0, 8.0, 9.5],   # Notas do segundo aluno
    [9.0, 8.5, 7.5, 6.0, 9.0]    # Notas do terceiro aluno
]

segunda_nota_primeiro_aluno = notas[0][1]

quinta_nota_terceiro_aluno = notas[2][4]

print(f"Segunda nota do primeiro aluno: {segunda_nota_primeiro_aluno}")
print(f"Quinta nota do terceiro aluno: {quinta_nota_terceiro_aluno}") 
'''
''' 
1 

alunos=[
[5.0,4.5,7.0,5.2,6.1], 
[2.1,6.5,8.0,7.0,6.7], 
[8.6,7.0, 9.1,8.7,9.3]
]
print(alunos[0][1])
print(alunos[2][4])
'''
'''
2 

def armazenar_nomes_e_idades():
    pessoas = []
    
    for i in range(10):
        nome = input(f"Digite o nome da pessoa {i+1}: ")
        idade = int(input(f"Digite a idade de {nome}: "))
        pessoas.append([nome, idade])
    
    # Encontrar a pessoa mais nova
    pessoa_mais_nova = min(pessoas, key=lambda x: x[1])

    print(f"\nA pessoa mais nova é {pessoa_mais_nova[0]} com {pessoa_mais_nova[1]} anos.")

# a funçãozinhaahh
armazenar_nomes_e_idades()
'''