#Exercício 60
#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

#5! = 5 x 4 x 3 x 2 x 1 = 120

valor = int(input("Informe o número para saber sua fatorial: "))
fim = 1
inicio = valor

while inicio > fim:
    inicio -= 1
    valor *= inicio

print(valor)



