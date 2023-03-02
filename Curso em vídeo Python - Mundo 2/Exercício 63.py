#Exercício 63
#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Exemplo:

#0 – 1 – 1 – 2 – 3 – 5 – 8

termos = int(input("Quantos termos da Sequência de Fibonacci você deseja? "))
termo1 = 0
termo2 = 1
contagem = 3
print(f"{termo1} > {termo2} >", end='')

while contagem <= termos:
    termo3 = termo1 + termo2
    print(f" {termo3} >", end='')
    termo1 = termo2
    termo2 = termo3
    contagem += 1

print(" Fim")