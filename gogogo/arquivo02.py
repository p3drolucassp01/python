primeiro = float(input("Informe o primeiro número: "))

segundo = float(input("Informe o segundo número: "))

terceiro = float(input("Informe o terceiro número: "))

if primeiro >= segundo and primeiro >= terceiro:
    print(f"O maior número é: {primeiro}")
elif segundo >= primeiro and segundo >= terceiro:
      
 print(f"O maior número é: {segundo}")
else:
    print(f"O maior número é: {terceiro}")