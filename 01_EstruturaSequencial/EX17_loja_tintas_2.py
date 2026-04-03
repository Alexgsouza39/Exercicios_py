"""
Docstring para Projetos.Python_exercicios.EX17_loja_tintas_2

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada e a quantidade de demãos de tinta. Considere que a cada litro de tinta, é possível pintar 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. O programa deverá informar ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

"""

area_pintura = float(input("Digite tamanho da area pintada m²: "))

litros = (area_pintura / 6.0) * 1.1 #10% de folga para imprevistos. Lembrando 6.0 area de cobertura é para forçar a divisão de float, caso contrário, o resultado seria um inteiro e não um float e 1.1 é para adicionar os 10% de folga.

latas = int(litros/ 18.0) #18.0 Capacidade do recipiente é para forçar a divisão de float, caso contrário, o resultado seria um inteiro e não um float.

galões = int(litros / 3.6) #3.6 Capacidade do recipiente é para forçar a divisão de float, caso contrário, o resultado seria um inteiro e não um float.

#calcular as latas
if litros % 18.0 !=0: 
    latas += 1

if litros % 3.6 !=0: 
    galões += 1

#calculo misturando latas e galões
mixlatas = int(litros / 18.0)
mixgaloes = int((litros - (mixlatas * 18.0)) / 3.6)

if ((litros - (mixlatas * 18.0)) % 3.6 !=0) > 0:# % e != para verificar se há sobra de tinta que não é suficiente para um galão inteiro, ou seja, se há necessidade de comprar um galão a mais.
    mixgaloes += 1


print(f"Quantidade de latas: {latas} - Preço total: R$ {latas * 80.0:.2f}")
print(f"Quantidade de galões: {galões} - Preço total: R$ {galões * 25.0:.2f}")
print(f"Quantidade de latas: {mixlatas} e galões: {mixgaloes} - Preço total: R$ {(mixlatas * 80.0) + (mixgaloes * 25.0):.2f}")