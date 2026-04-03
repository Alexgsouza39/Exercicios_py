# Media Aluno

nota1 = float(input("Informe 1ª Nota: "))
nota2 = float(input("Informe 2ª Nota: "))

media = (nota1+nota2) / 2 #Formula para média

print(f" A média do aluno é: {media}")

if media == 10:
    print("Aprovado com nota máxima!")
elif media >= 7:
    print("Aprovado!")
else:
    print ("Reprovado")