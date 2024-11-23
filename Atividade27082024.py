a = float (input("Digite o primeiro numero: "))
b = float (input("Digite o segundo numero: "))
opcao = int (input("Escolha uma opção\nSoma 1\nSubtração 2\nMutiplicação 3\nDivisão 4\nDigite: "))

if opcao == 1:
 print(a+b)

elif opcao == 2:
    print(a-b)

elif opcao == 3:
    print(a*b)

elif opcao == 4:
    print(a/b)  

else: 
   print("Opção invalida, tente novamente!")
    
