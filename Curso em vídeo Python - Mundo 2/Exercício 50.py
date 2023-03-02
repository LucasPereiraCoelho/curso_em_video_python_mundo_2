#Exercício 50 
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for n in range (1, 6):
    num = int(input("Informe um número inteiro: "))

    if num % 2 == 0:
        soma += num

print(soma)