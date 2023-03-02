#Exercício 52
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Informe um número para saber se é primo ou não: "))
total = 0

for n in range(1, num + 1):
    if num % n == 0:
        print("\033[33m", end='',)
        total += 1
    else:
        print("\033[31m", end='')
    
    print(n, end='')

if total > 2:
    print(" \033[mNúmero não primo.")
if total == 2:
    print(" \033[mNúmero primo!")
else:
    print(" \033[mNúmero não primo.")

print(f"\033[mO número {num} foi divisível {total} vezes.")

