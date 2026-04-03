# taxa_de_transferencia.py

transferencia = float(input("Digite a taxa de transferencia MB: "))
velocidade = float(input("Digite a velocidadede de transferencia Mbps: "))

transferencia_bits = transferencia * 1024 * 1024 * 8 # Convertendo MB para bits
tempoSegundos = transferencia_bits / (velocidade * 1024 * 1024) # Convertendo Mbps para bits por segundo e calculando o tempo
tempoMinutos = tempoSegundos / 60 # Convertendo segundos para minutos

print(f"Tempo de tranasferecia: {tempoSegundos:.2f} Segundos")#imprime tempo segundos
print(f"Tempo de tranasferecia: {tempoMinutos:.2f} Minutos") #imprime tempo minutos   
