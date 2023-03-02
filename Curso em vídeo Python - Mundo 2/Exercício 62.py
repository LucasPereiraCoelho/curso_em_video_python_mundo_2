#Exercício 62
#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

inicio = int(input("Informe o inicío da PA: "))
razao = int(input("Informe a razão: "))
termo = 10
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo)
        termo += razao
        cont += 1
    mais = int(input("Quantos termos a mais você deseja? "))
