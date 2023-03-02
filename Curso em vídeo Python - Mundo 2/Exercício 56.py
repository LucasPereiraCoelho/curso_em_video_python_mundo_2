#Exercício 56
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#a) A média de idade do grupo;
#b) Qual é o nome do homem mais velho;
#c) Quantas mulheres têm menos de 20 anos.

totalidade = 0
meninas = 0
velho = 0
nomevelho = ""

for n in range(1, 5):
    nome = str(input("Informe o seu nome: ")).strip()
    idade = int(input("Informe a sua idade: "))
    sexo = str(input("Informe o seu sexo (M para masculino e F para feminino): ")).strip().upper()

    totalidade += idade
    

    if sexo == "F":
        if idade < 20:
            meninas += 1

    if sexo == "M":
        if  idade > velho:
            velho = idade
            nomevelho = nome



print(f"A média de idade do grupo é de {totalidade / 4} anos.")
print(f"Tem um total de {meninas} mulheres com menos de 20 anos.")
print(f"O homem mais velho tem {velho} anos e se chama {nomevelho}.")

