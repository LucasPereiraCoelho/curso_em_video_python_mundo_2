#Exercício 54
#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
menor = 0
maior = 0

for n in range(1, 8):
    ano = int(input("Informe o ano do seu nascimento: "))

    if atual - ano < 18:
        menor += 1
    elif atual - ano > 18:
        maior += 1

print(f"Teve um total de {menor} pessoas menores de idade.")
print(f"Teve um total de {maior} pessoas maiores de idade.")

