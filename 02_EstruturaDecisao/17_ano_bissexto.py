# Programa para verificar se um ano é bissexto seguindo as regras do calendário gregoriano

# Recebe a entrada do usuário e converte para número inteiro (int)
ano = int(input('Informe um ano: '))

# Inicializamos uma variável 'flag' como False por padrão
bissexto = False

# Primeira condição: Um ano bissexto precisa ser divisível por 4 (resto da divisão % por 4 igual a 0)
if (ano % 4 == 0):
    bissexto = True
    
    # Segunda condição (Exceção): Se o ano for divisível por 100, ele NÃO é bissexto...
    # ...A MENOS que ele também seja divisível por 400. 
    # O código abaixo verifica se ele falha na regra do 400 enquanto cai na do 100.
    if (ano % 100 == 0) and (ano % 400 != 0):
        bissexto = False

# Saída de dados baseada no estado final da variável booleana 'bissexto'
if (bissexto):
    print ('O ano é BISSEXTO')
else:
    print ('O ano NÃO é BISSEXTO')