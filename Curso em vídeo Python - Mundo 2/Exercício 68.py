#Exercício 68
#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitoria = 0

while True:

    escolha = str(input("""\nVamos jogar par ou ímpar.
\nQual você escolhe (P / I): """)).strip().upper()[0]
    jogador = int(input("\nJogue um número: "))
    comp = randint(1,10)
    soma = jogador + comp
    
    if escolha == "P":
        if soma % 2 == 0:
            print(f"\nEu joguei {comp} e você jogou {jogador} a soma disso é par ({soma}), portanto você ganhou.")
            vitoria += 1
        else:
            print(f"\nEu joguei {comp} e você jogou {jogador} a soma disso é ímpar ({soma}), portanto você perdeu.")
            break
    
    if escolha == "I":
        if soma % 2 != 0:
            print(f"\nEu joguei {comp} e você jogou {jogador} a soma disso é ímpar ({soma}), portanto você ganhou.")
            vitoria += 1
        else:
            print(f"\nEu joguei {comp} e você jogou {jogador} a soma disso é par ({soma}), portanto você perdeu.")
            break


print(f"\nVocê ganhou {vitoria} vezes")
       
       

    
    
