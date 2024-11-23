'''print("--------------------sistema de cadastro--------------------")'''
def validar_nome(nome):
    return len(nome) <= 30 and nome.isalpha()
print(validar_nome('Pedro'))

def validar_idade(idade):
    try:
        idade = int(idade)
        return 18 <= idade <= 65
    except ValueError:
        return False
    print(validar_idade(21))
    
    '''

nome = input("Digite o nome do cliente: ")
if not validar_nome(nome):
    print("Erro: O nome deve ter até 30 caracteres e não conter caracteres especiais.")
else:
    idade = input("Digite a idade do cliente: ")
    if not validar_idade(idade):
        print("Erro: A idade deve ser um número entre 18 e 65.")
    else:
        print(f"Cliente cadastrado com sucesso! Nome: {nome}, Idade: {idade}")'''
