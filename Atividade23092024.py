'''
class pessoa:
    def __init__(self,nome,sobrenome,cpf):
         self.nome=nome
         self.sobrenome=sobrenome
         self.cpf=cpf
    def nome_completo():
             return 'f{self.nome} {self.sobrenome}'
    

class Cliente(pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        pessoa.__init__(self,nome,sobrenome,cpf)
        self.renda=renda

    def nome_completo(self):
        return f'nome_compelto:{self.nome} {self.sobrenome},renda: {self.renda}, cpf: {self.cpf}'        
class Funcionarios(pessoa):
    
    def __init__(self, nome, sobrenome, cpf, matricula):
        pessoa.__init__(self,nome,sobrenome,cpf)
        self.matricula = matricula
        
    def nome_completo(self):
        return f'nome_funcionario: {self.nome} {self.sobrenome}, cpf: {self.cpf}, matricula: {self.matricula}'

Cliente1=Cliente('Matheus', 'Alves', '00000000005', 1000)
Funcionario1=Funcionarios('Ana', 'Oliveira', '5888888888', 8)

print(Cliente1.nome_completo())
print(Funcionario1.nome_completo())
'''

'''from heranca import Cliente

Cliente1=Cliente('Matheus', 'Alves', '00000000005', 1000)
print(Cliente1.nome_completo())
'''

#atividade heranca

'''
Professor (nome, idade, cpf, telefone, email, disciplina)
Aluno (nome, idade, cpf, telefone, email, escolaridade)
'''

class Professor:
    def __init__(self, nome, idade, cpf, telefone, email, disciplina):
        self.nome=nome
        self.idade= idade
        self.cpf=cpf
        self.telefone=telefone
        self.email=email
        self.disciplina=disciplina

    def mostra_nomeP(self):
        
        return f'Nome do professor:{self.nome}'
        
    def mostra_Disciplina(self):

        return f'Disciplina: {self.disciplina}'

class Aluno:
    def __init__(self, nome, idade, cpf, telefone, email, escolaridade):
        self.nome=nome
        self.idade= idade
        self.cpf=cpf
        self.telefone=telefone
        self.email=email
        self.escolaridade=escolaridade

    def mostra_nomeA(self):
        
        return f'Nome do aluno: {self.nome}'

    def Mostra_escolaridade(self):

        return f'Escolaridade: {self.escolaridade}'
     
Professor1= Professor('Pedro', 36, '10067842594', 81993637548, 'ph294@gmail.com', 'História')
Aluno1= Aluno('Jose', 15, '13493524598', 819345934589, 'joSe3949@gmail.com', 'ensino medio')

print(Professor1.mostra_nomeP())
print(Professor1.mostra_Disciplina())
print('\n')
print(Aluno1.mostra_nomeA())
print(Aluno1.Mostra_escolaridade())
