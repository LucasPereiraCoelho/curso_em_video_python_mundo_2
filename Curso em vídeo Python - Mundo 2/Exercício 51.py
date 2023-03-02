#Exercício 51
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio = int(input("Informe o inicío da PA: "))
razao = int(input("Informe a razão: "))
decimo = inicio + (10 - 1) * razao

for n in range (inicio, decimo + razao, razao):
    print(f"{n}")
    
