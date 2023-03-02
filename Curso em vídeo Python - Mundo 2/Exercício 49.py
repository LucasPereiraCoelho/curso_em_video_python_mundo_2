#Exercício 49
#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Informe um número que você deseja para saber sua tabuada: "))

for n in range (1, 11):
    print(f"{n} x {num} = {n * num}")