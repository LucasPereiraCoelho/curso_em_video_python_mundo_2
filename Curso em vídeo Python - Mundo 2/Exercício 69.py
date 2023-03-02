#Exercício 69
#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

maiores = 0
homens = 0
mulher20 = 0

while True:

    idade = int(input("Informe a sua idade: "))
    sexo = str(input("Informe o seu sexo (M / F): ")).strip().upper()[0]

    if idade > 18:
        maiores += 1
    
    if sexo == "M":
        homens += 1

    if sexo == "F":
        if idade < 20:
            mulher20 += 1

    cond = str(input("Você deseja continuar(S / N): ")).strip().upper()[0]

    if cond == "N":
        break

print(f"""Das pessoas cadastradas, {maiores} tinham mais que 18 anos.
{homens} homens foram cadastrados.
E {mulher20} mulheres com menos de 20 anos foram cadastradas.""")