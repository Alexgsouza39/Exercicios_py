# Calcular salário
'''
Docstring para Projetos.Python_exercicios.EX15_salario

Faça um programa para calcular o salário de um funcionário, considerando o valor por hora e a quantidade de horas trabalhadas no mês. O programa deve calcular o salário bruto, o imposto de renda (11%), o INSS (8%) e o sindicato (5%). Por fim, deve mostrar o salário líquido do funcionário.

variaveis:
- valorPorHora: float introduzido pelo usuario
- horasTrabalhadas: float introduzido pelo usuario
- salarioBruto: float calculado a partir do valorPorHora e horasTrabalhadas
- impostoRenda: float  calculado a partir do salarioBruto
- inss: float calculado a partir do salarioBruto
- sindicato: float calculado a partir do salarioBruto
- salarioLiquido: float calculado a partir do salarioBruto e dos descontos

imprimir:
- Salario Bruto: salarioBruto
- Imposto de Renda: impostoRenda
- INSS: inss
- Sindicato: sindicato
- Salario Liquido: salarioLiquido
'''

valorPorHora = float(input('Quanto voce ganha por hora: '))
horasTrabalhadas = float(input('Quantas horas voce trabalhou no mes: '))

salarioBruto = round(float(valorPorHora * horasTrabalhadas), 2)
impostoRenda = round(float(salarioBruto * 0.11), 2)
inss = round(float(salarioBruto * 0.08), 2)
sindicato = round(float(salarioBruto * 0.05), 2)
salarioLiquido = round(float(salarioBruto - impostoRenda - inss - sindicato), 2)

print(
    'Salario Bruto:', salarioBruto,
    'Imposto de Renda:', impostoRenda,
    'INSS:', inss,
    'Sindicato:', sindicato,
    'Salario Liquido:', salarioLiquido
)


