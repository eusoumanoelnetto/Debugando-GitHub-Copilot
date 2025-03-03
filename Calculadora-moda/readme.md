# Calculadora de Moda

## Descrição
Você está desenvolvendo uma calculadora de moda e se deparou com alguns erros no código. Seu objetivo é corrigir os problemas para que a calculadora funcione corretamente. No código original, há erros de lógica e de sintaxe que impedem de calcular a moda corretamente.

Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode sugerir correções de código.

Este é um projeto da Dio.

## Entrada
A entrada deve receber uma sequência de números inteiros separados por espaço. O programa deve ser capaz de processar esses números e contar quantas vezes cada valor aparece.

## Saída
A saída deverá retornar o número que aparece com maior frequência (a moda).

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                | Saída |
|------------------------|-------|
| 1 2 2 3 3 3 4          | 3     |
| 1 1 4 2 3 3 4 4        | 4     |
| 7 8 9 7 7 8 8 9 9 9    | 9     |

## Estrutura de Arquivos

- `codigo-bugado.py`: Contém o código original com erros.
- `debugando.py`: Contém o código corrigido.

## Código Original (codigo-bugado.py)
```python
def calcular_moda(numeros):
    contagem = {}
    for numero in numeros:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    moda = max(contagem, key=contagem.get)
    return moda

# Entrada do usuário
entrada = input()
numeros = list(map(int, entrada.split()))

print(calcular_moda(numeros))
