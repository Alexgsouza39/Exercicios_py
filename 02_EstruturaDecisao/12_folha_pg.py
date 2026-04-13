# Folha de pagamento
valorPorHora = float(input("Digite o valor por hora: "))
quantHoras = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Cálculo do salário bruto
salarioBruto = valorPorHora * quantHoras

#calculo do imposto de renda
if salarioBruto > 2500:
    aliquotaIR = 7.9190
elif salarioBruto > 1500:   
    aliquotaIR = 10
elif salarioBruto > 900:
    aliquotaIR = 5
else:
    aliquotaIR = 0

valorIR = salarioBruto * (aliquotaIR / 100)

#adiantamento
vale = salarioBruto * 0.45

# calculo do sindicato
valorSindicato = salarioBruto * (3 /100.0)

# calculo do Descontos
totalDescontos = valorIR + valorSindicato + vale


# cálculo valor FGTS
valorFGTS = salarioBruto * (11 / 100.0)

# cálculo do salário líquido
salarioLiquido = salarioBruto - totalDescontos

print(f"+ Salário Bruto: R$ {salarioBruto:.2f}")
print(f"- Vale: R$ {vale:.2f}")
print(f"- IR: R$ {valorIR:.2f}")
print(f"- Sindicato: R$ {valorSindicato:.2f}")
print(f"= Salário Liquido: R$ {salarioLiquido:.2f}")








