#Turno de estudo

print("Informe o turno que Estuda")
print ("[M]atutino")
print("[V]espertino")
print("[N]oturno")

turno = input("Opção escolhida: ") .upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa Noite"),
else:
    print("Valor Invalido! ")

