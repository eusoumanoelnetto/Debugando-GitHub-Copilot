def verificar_anagrama(palavra1, palavra2):
    # Remove espaços e converte para letras minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    # Verifica se as palavras ordenadas são iguais
    return sorted(palavra1) == sorted(palavra2)

def main():
    entrada = input().strip()

    palavras = entrada.split()
    if len(palavras) != 2:
        print("Entrada inválida. Forneça duas palavras separadas por espaço.")
        return

    palavra_a, palavra_b = palavras[0], palavras[1]

    if verificar_anagrama(palavra_a, palavra_b):
        print("Verdadeiro")
    else:
        print("Falso")

if __name__ == "__main__":
    main()
