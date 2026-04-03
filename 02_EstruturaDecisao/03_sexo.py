# Sexo

sexo = input("Informe F para Feminino e M para Masculino: ") #Solicitação ao usuario

if sexo.upper() == "M":# Condição se input = M
    print("MASCULINO") # Imprima Masculino
elif sexo.upper() == "F": # Condição se input = M
    print("FEMININO") # Imprima Feminino
else: 
    print("Sexo inválido!") #Condição se input não atender a condição imprima sexo invalido 