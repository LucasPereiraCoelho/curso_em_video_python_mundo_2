#Exercício 55
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0

for n in range(0, 5):
    peso = float(input(f"Informe o peso da pessoa {n + 1}: "))

    if n == 0:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    
print(f"O menor peso foi de {menor}Kg", end='')
print(f" E o maior foi de {maior}Kg")

