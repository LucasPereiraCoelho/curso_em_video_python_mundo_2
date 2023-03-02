#Exercício 65
#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = 0
menor = 0
total = 0
contador = 0

while True:
    num = int(input("Informe um número: "))
    total += num
    contador += 1

    if menor == 0:
        menor = num
    
    elif maior == 0:
        maior = num


    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    a = str(input("Deseja continuar? (S/N): ")).strip().upper()

    if a == "S":
        continue
    elif a == "N":
        break
    else:
        print("Valor inválido")
        break

print("A média entre os valores digitados é de %.2f"%(total / contador))
print(f"O maior valor digitado foi de {maior}", end='')
print(f" e o menor foi de {menor}.")


