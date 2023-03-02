#Exercício 64
#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

contador = 0
soma = 0

while True:

    n = int(input("Informe um valor inteiro (999 para sair): "))
    
    if n == 999:
        break
    
    soma += n
    contador += 1

    

print(f"A soma dos números digitados é de: {soma}")
print(f"A quantidade de números digitados foi de: {contador}")