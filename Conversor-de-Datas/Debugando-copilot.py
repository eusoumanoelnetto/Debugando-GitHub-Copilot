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
