
# Exercício 6: Calcular a área de um círculo metodo 1: usando o valor de pi definido como 3.1415 manual.
p=3.1415

raio = float('1')

area = p * raio ** 2
print('A área do círculo é: ', area)

# Exercício 6: Calcular a área de um círculo metodo 1: usando o valor de pi definido como 3.1415 manual com 4 casas decimais.
print('A área do círculo é: ', round(area, 4))

# Exercício 6: Calcular a área de um círculo metodo 2: usando o valor de pi da biblioteca math mais preciso.
import math

raio = float('2.5')
area = math.pi * raio ** 2
print('A área do círculo é: ', area)

# Exercício 6: Calcular a área de um círculo metodo 3: usando o valor de pi da biblioteca math mais preciso com 4 casas decimais.
print('A área do círculo é: ', round(area, 4))