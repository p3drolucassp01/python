Nota1 = float(input('Digite sua primeira nota: '))
Nota2 = float(input('Digite sua segunda nota: '))

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"

result = (Nota1 + Nota2) /2

if result >= 7.0:
    print(f"{GREEN}APROVADO{RESET}")
elif 5.0 <= result < 7.0: 
    print(f"{YELLOW}RECUPERAÇÃO{RESET}")
else:
    print(f"{RED}REPROVADO{RESET}")
    
 