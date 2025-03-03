# Conversor de Datas

## Descrição
Você recebeu um código que faz a conversão de datas do formato "yyyy-mm-dd" para o formato "dd/mm/yyyy", mas ele contém erros de lógica e sintaxe. O objetivo desse desafio é debugar o código do template e corrigir o problema, fazendo com que ele converta corretamente datas do formato "yyyy-mm-dd" para o formato "dd/mm/yyyy".

Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode sugerir correções de código.

## Entrada
A entrada será uma string representando uma data no formato "yyyy-mm-dd" (exemplo: 2024-12-25).

## Saída
Deverá retornar a data convertida para o formato "dd/mm/yyyy". Se a entrada não estiver no formato correto, deve ser retornada a mensagem "Formato de data inválido."

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada    | Saída        |
|------------|--------------|
| 2024-12-25 | 25/12/2024   |
| 2020-01-01 | 01/01/2020   |
| 1999-07-04 | 04/07/1999   |

## Código
O código a ser corrigido está no arquivo [Debugando.py](Debugando.py):

```python
def converter_para_dia_mes_ano(data_str):
    try:
        # Divide a string e valida o formato
        ano, mes, dia = data_str.split("-")
        if len(ano) == 4 and len(mes) == 2 and len(dia) == 2 and ano.isdigit() and mes.isdigit() and dia.isdigit():
            return f"{dia}/{mes}/{ano}"
        else:
            return "Formato de data inválido"
    except ValueError:
        return "Formato de data inválido"

# Entrada do usuário (sem mensagem adicional no input)
data_input = input()

# Verifica e imprime o resultado
if "-" in data_input:
    print(converter_para_dia_mes_ano(data_input))
else:
    print("Formato de data inválido")