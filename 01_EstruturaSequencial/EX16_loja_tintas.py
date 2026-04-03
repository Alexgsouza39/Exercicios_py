"""# Loja de Tintas
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total."""

area_pintura = float(input("Digite o tamanho da área a ser pintada em m²: "))

cobertura = 6 #m²/ litro
lata_litros = 18 #Qtd litros por lata
preco_lata = 80 #Preço por lata

litros_necessarios = area_pintura / cobertura #calculo da qtd de litros necessários
lata_necessarias = litros_necessarios / lata_litros #calculo da qtd de latas necessarias
preco_total =(litros_necessarios / lata_litros) * preco_lata #calculo de preco total

if lata_necessarias % 1 !=0: #verificar se a quantidade de lata necessária é um número inteiro e arredonda para cima.
    lata_necessarias = int(lata_necessarias) + 1

print(f"Quantidade de litros necessários: {litros_necessarios}")
print(f"Quantidade de latas necessárias: {lata_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")
