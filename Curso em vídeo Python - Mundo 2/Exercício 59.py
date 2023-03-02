#Exercício 59
#Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

progama = True

while progama:

    op = int(input("""\n[ 1 ] Somar
    \n[ 2 ] Multiplicar
    \n[ 3 ] Maior entre eles
    \n[ 4 ] Novos Valores
    \n[ 5 ] Sair.
    
    \nQual opção você deseja: """))

    if op == 1:
        print(f"\n{num1} + {num2} = {num1 + num2}")
        continue
    elif op == 2:
        print(f"\n{num1} x {num2} = {num1 * num2}")
        continue
    elif op == 3:
        if num1 > num2:
            print(f"\nO maior é: {num1}")
        elif num2 > num1:
            print(f"\nO maior é {num2}")
        else:
            print(f"\nSão iguais")
        continue
    elif op == 4:
        num1 = int(input("\nInforme o primeiro valor: "))
        num2 = int(input("Informe o segundo valor: "))
        continue
    else:
        print("\nSaindo")
        progama = False

print("\nFim")

        