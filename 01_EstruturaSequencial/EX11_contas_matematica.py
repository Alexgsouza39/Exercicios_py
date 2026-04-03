"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""
import math

num1 = int(input('Inserir primeiro nunero: '))
num2 = int(input('Inserir segundo nunero: '))
r = float(input('Inserir numero real: '))

res1 = (num1*2 + num2/2)
res2 = (3* num1) + r
res3 = (r)** 3

print('Ola este é o dobro do primeiro com metade do segundo: ', f'{res1:.2f}')
print('Ola esta é a soma do triplo do primeiro com o terceiro: ', f'{res2:.2f}')
print('Ola este é o terceiro elevado ao cubo: ', f'{res3:.2f}')



