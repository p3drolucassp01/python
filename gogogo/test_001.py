def maior_numero(primeiro, segundo, terceiro):
    if primeiro >= segundo and primeiro >= terceiro:
        return primeiro
    elif segundo >= primeiro and segundo >= terceiro:
        return segundo
    else:
        return terceiro


if __name__ == "__main__":
    primeiro = float(input("Informe o primeiro número: "))
    segundo = float(input("Informe o segundo número: "))
    terceiro = float(input("Informe o terceiro número: "))
    print(f"O maior número é: {maior_numero(primeiro, segundo, terceiro)}")

