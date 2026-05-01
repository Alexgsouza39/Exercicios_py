# Solicita a entrada do usuário
# '=' é o operador de ATRIBUIÇÃO: guarda o texto digitado na variável 'data'
data = input('Informe uma data no formato dd/mm/yyyy: ') 

# Extrai partes da string usando fatiamento (slicing) e converte para inteiros
# '[]' e ':' são operadores de FATIAMENTO: extraem pedaços da string por índice
dia = int(data[0:2]) # Pega do índice 0 até o 1
mes = int(data[3:5]) # Pega do índice 3 até o 4
ano = int(data[6:])  # Pega do índice 6 até o fim

print(dia, mes, ano)

# Lógica para determinar se o ano é bissexto (Regras do Calendário Gregoriano)
bissexto = False
# '%' é o operador MÓDULO: retorna o resto da divisão. '==' é o operador de IGUALDADE
if (ano % 4 == 0): # Se o resto da divisão do ano por 4 for zero
    bissexto = True
    # 'and' é o operador LÓGICO E: ambas condições devem ser verdadeiras
    # '!=' é o operador de DIFERENÇA (não igual)
    if (ano % 100 == 0) and (ano % 400 != 0): # Se divisível por 100 E NÃO por 400
        bissexto = False

valida = True
# Verificação para meses que possuem 31 dias
# 'in' é o operador de PERTENCIMENTO: verifica se o valor está na sequência
if (mes in (1, 3, 5, 7, 8, 10, 12)):
    # '<' e '>' são operadores RELACIONAIS. 'or' é o operador LÓGICO OU
    if (dia < 1) or (dia > 31): # Se o dia for menor que 1 OU maior que 31
        valida = False
# Verificação para meses que possuem 30 dias
elif (mes in (4, 6, 9, 11)):
    if (dia < 1) or (dia > 30):
        valida = False
# Lógica específica para Fevereiro (mês 2)
else: 
    if (bissexto):
        if (dia < 1) or (dia > 29): # Fevereiro bissexto tem 29 dias
            valida = False
    else:
        if (dia < 1) or (dia > 28): # Fevereiro comum tem 28 dias
            valida = False

# Impressão do resultado final baseado na flag 'valida'
if (valida):
    print ('Data VALIDA')
else:
    print ('Data INVALIDA')