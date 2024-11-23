def calcular_soma(N, M):
    if N < M:
        if N % 2 == 0:
            NRO = N + 1
        else:
            NRO = N
        
        SOMA = 0
        
        while NRO <= M:
            if NRO > 0:
                SOMA += NRO
            NRO += 2
        
        return N, M, SOMA
    else:
        return "INTERVALO INCORRETO"
