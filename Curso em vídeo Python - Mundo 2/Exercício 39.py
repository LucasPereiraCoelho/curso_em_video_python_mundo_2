#Exercício 3 
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input("Informe o ano do seu nascimento: "))
idade = date.today().year - ano

if idade < 18:
    print("Voçê ainda vai se alistar.")
    print(f"Falta um total de {18 - idade} ano(s) para você se alistar")
elif idade == 18:
    print("Está na hora exata de você se alistar.")
else:
    print("Já passou o tempo de você se alistar.")
    print(f"Ja passou {idade - 18} ano(s) desde que você estava no prazo de alistamento.")




