#Calcule a multa de um pescador por exceder o peso da pescaria

peso = float(input('Informe o peso dos peixes pescados: '))
multa_por_kilo = 4.0
peso_max = 50.0

if (peso > peso_max):
    excesso = peso - peso_max
    print(f'O peso excede a capacidade: ', excesso)
    print(f'Valor multa por excesso', excesso * multa_por_kilo)
else: 
    print("Não houve excesso de peso")