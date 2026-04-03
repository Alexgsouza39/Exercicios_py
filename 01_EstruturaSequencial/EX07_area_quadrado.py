
lado= '2'
area_quadrado = float(lado) ** 2
dobro_area = area_quadrado * 2

print('A área do quadrado é:',f'{area_quadrado:.2f}')
print('O dobro da área do quadrado é:',f'{dobro_area:.2f}')
# O código acima calcula a área de um quadrado com lado 2 e o dobro dessa área, exibindo os resultados formatados com duas casas decimais.

# Outra forma de calcular a área do quadrado e o dobro da área, utilizando uma função:

def calcular_area_quadrado(lado):
    area = lado ** 2
    dobro_area = area * 2
    return area, dobro_area
area_quadrado, dobro_area = calcular_area_quadrado(float(lado))

print('A área do quadrado é:',f'{area_quadrado:.2f}')
print('O dobro da área do quadrado é:',f'{dobro_area:.2f}')
# Neste código, a função calcular_area_quadrado recebe o lado do quadrado como argumento, calcula a área e o dobro da área, e retorna ambos os valores. Em seguida, os resultados são exibidos formatados com duas casas decimais.

#outra forma, utilizando uma função lambda:
calcular_area_quadrado = lambda lado: (lado ** 2, (lado ** 2) * 2)
area_quadrado, dobro_area = calcular_area_quadrado(float(lado))
print('A área do quadrado é:',f'{area_quadrado:.2f}')
print('O dobro da área do quadrado é:',f'{dobro_area:.2f}')
# Neste código, a função lambda calcular_area_quadrado recebe o lado do quadrado como argumento e retorna uma tupla contendo a área do quadrado e o dobro da área. Os resultados são exibidos formatados com duas casas decimais.

