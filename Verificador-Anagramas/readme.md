# Verificador de Anagramas

## Descrição
O objetivo desse desafio é identificar e corrigir erros em um programa que verifica se duas palavras são anagramas. Anagramas são palavras que contêm as mesmas letras, mas em uma ordem diferente. O programa precisa exibir "Verdadeiro" se as palavras forem anagramas e "Falso" caso contrário. No entanto, o programa contém alguns erros de lógica e sintaxe que precisam ser corrigidos.

Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode sugerir correções de código.

## Entrada
A entrada consistirá de duas palavras (A e B), fornecidas em uma única linha, separadas por um espaço. Por exemplo: `ouvir virou`.

## Saída
O programa deve retornar uma mensagem indicando se as palavras são anagramas ou não:

- "Verdadeiro" (se as palavras forem anagramas).
- "Falso" (se as palavras não forem anagramas).

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada      | Saída       |
|--------------|-------------|
| ouvir virou  | Verdadeiro  |
| gato pato    | Falso       |
| amor roma    | Verdadeiro  |

## Estrutura de Arquivos

- `verificador-anagramas.py`: Contém o código original com erros.
- `codigo-debugado.py`: Contém o código corrigido.

## Código Original (verificador-anagramas.py)
```python
def sao_anagramas(palavra1, palavra2):
    if sorted(palavra1) == sorted(palavra2):
        return "Verdadeiro"
    else:
        return "Falso"

# Entrada do usuário
entrada = input()
palavra1, palavra2 = entrada.split()

print(sao_anagramas(palavra1, palavra2))