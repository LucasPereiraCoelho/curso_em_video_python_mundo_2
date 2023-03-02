#Exercício 45 
#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep



lista = ["PEDRA", "PAPEL", "TESOURA"]

pc = choice(lista)
vencedor = ""


while True:

    jogador = int(input("""\nVamos jogar Jokenpô! Suas opções:\n 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
[ 4 ] SAIR
\nQual você escolhe? """))

    if jogador == 4:
        print("\nVolte outra hora!")
        break
    elif jogador != 1 and jogador != 2 and jogador != 3:
        print("Valor inválido, tente novamente.")
        sleep(2)
        continue

        

    if pc == "PEDRA":
        if jogador == 1:
            jogador = "PEDRA"
            vencedor = "EMPATE!"
        elif jogador == 2:
            jogador = "PAPEL"
            vencedor = "Você Venceu!"
        elif jogador == 3:
            jogador = "TESOURA"
            vencedor = "CPU Venceu!"
        
        

    if pc == "PAPEL":
        if jogador == 1:
            jogador = "PEDRA"
            vencedor = "CPU Venceu!"
        elif jogador == 2:
            jogador = "PAPEL"
            vencedor = "EMPATE!"
        elif jogador == 3:
            jogador = "TESOURA"
            vencedor = "Você Venceu!"

        

    if pc == "TESOURA":
        if jogador == 1:
            jogador = "PEDRA"
            vencedor = "Você Venceu!"
        elif jogador == 2:
            jogador = "PAPEL"
            vencedor = "CPU Venceu!"
        elif jogador == 3:
            jogador = "TESOURA"
            vencedor = "EMPATE!"

    

    print("\nJO...")
    sleep(1)
    print("KEN...")
    sleep(1)
    print("PÔ!")
    sleep(1)

    print (f"\nVocê escolheu {jogador}.")
    print (f"A CPU escolheu {pc}.")
    print (f"portanto {vencedor}.")

    repetir = str(input("\nDeseja Tentar de novo? (Sim ou Não): ")).strip()

    repetir = repetir.upper()

    if repetir == "SIM" or repetir == "S":
        continue
    elif repetir == "NÃO" or repetir == "NAO" or repetir == "N":
        print("Volte outra hora!")
    else:
        print("Digitação inválida, retornando ao início.")
        sleep(2)
        continue

   
    break


    
       

        
