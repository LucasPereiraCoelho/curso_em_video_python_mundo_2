#Exercício 57
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = str(input("Informe o seu sexo (M/F) : ")).strip().upper()

    if sexo == "M":
        print("Parabéns você é homem!")

    elif sexo == "F":
        print("parabéns você é mulher!")

    else:
        sexo = print("Opção inválida")
        continue   

