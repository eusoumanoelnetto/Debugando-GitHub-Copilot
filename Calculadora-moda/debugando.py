def calcular_moda(lista):
    frequencias = {}
    # Conta a frequência de cada número
    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    
    # Encontra a maior frequência
    maior_frequencia = max(frequencias.values())
    # Lista todos os números que possuem a maior frequência
    modas = [num for num, freq in frequencias.items() if freq == maior_frequencia]
    
    return modas

# Lê a entrada
entrada = input().strip()
try:
    dados = list(map(int, entrada.split()))
    if not dados:
        raise ValueError("Lista vazia.")
    # Calcula as modas
    modas = calcular_moda(dados)
    # Verifica se há mais de uma moda e imprime o resultado
    if len(modas) > 1:
        print(" ".join(map(str, modas)))
    else:
        print(modas[0])
except ValueError:
    print("Entrada inválida. Forneça números inteiros separados por espaço.")
