#Exercício 37 
#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#1 para binário; 
#2 para octal;
#3 para hexadecimal.

num = int(input("Informe um número inteiro: "))
base = int(input("Informe qual base de conversão você deseja 1 para binário, 2 para octal e 3 para hexadecimal: "))

if base == 1:
    print(f"O número digitado em binário é: {bin(num)[2:]}")
elif base == 2:
    print(f"O número digitado em octal é {oct(num)[2:]}")
elif base == 3:
    print(f"O número digitado em hexadecimal é: {hex(num)[2:]} ")
else:
    print("Valor inválido.  ")
