#Exercício 70
#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

contador1000 = 0
total = 0
cont = 0
nomebarato = ""


while True:
    nome = str(input("Informe o nome do produto: ")).strip()
    valor = float(input("Informe o valor do produto: "))
    cont += 1
    total += valor

    if valor > 1000:
        contador1000 += 1

    if cont == 1 or valor < barato:
        barato = valor
        nomebarato = nome
    
    cond = str(input("Você deseja continuar (S / N): ")).strip().upper()[0]

    if cond == "N":
        break

print(f"""Total gasto na compra foi de R${total:.2f}
{contador1000} produtos custam mais de 1000 reais.
O produto mais barato foi {nomebarato}.""")
    



