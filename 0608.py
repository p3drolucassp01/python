nome = str (input("Nome do aluno(a): "))
nota1 = float (input("Informe a nota da primeira unidade do aluno(a): "))
nota2 = float (input("Informe a nota da segunda unidade unidade do aluno(a): "))
nota3 = float (input("Informe a nota da terceira unidade do aluno(a): "))
nota4 = float (input("Informe a nota da quarta unidade do aluno(a): "))

mediafinal = int (nota1+nota2+nota3+nota4)/4

print("Media final do aluno(a)",nome,": ", mediafinal)
 
if (mediafinal >= 7):{
     print("Aprovado!")
}
else:{ 
 print("Reprovado!")
}