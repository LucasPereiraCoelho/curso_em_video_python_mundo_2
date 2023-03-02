#Exercício 61
#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

inicio = int(input("Informe o inicío da PA: "))
razao = int(input("Informe a razão: "))
termos = 0

while termos != 10:
    print(inicio)
    inicio += razao
    termos += 1
