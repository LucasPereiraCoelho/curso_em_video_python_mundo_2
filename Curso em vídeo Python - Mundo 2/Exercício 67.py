#Exercício 67
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

while True:

    num = int(input("Informe um valor para saber a sua tabuada(insira um valor negativo para encerrar oo progama): "))

    if num < 0:
        break

    for n in range(1,11):
        print(f"{num} x {n} = {num * n}")

    