#Exercício 58
#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num = randint(0, 10)
certo = False
contador = 0

while not certo:
    vlr = int(input("Chute um valor de 0 a 10: "))
    contador += 1
    if vlr == num:
        certo = True
        print("Parabéns você acertou.")
    else:
        print("Não era esse, tente outro...")
        
print(f"Foram necessários {contador} chutes para você vencer!")