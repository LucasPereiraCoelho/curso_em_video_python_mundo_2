#Exercício 44
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

preco = float(input("Informe o valor das suas compras: "))

modo = int(input("""\nFORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque: Desconto de 10%
[ 2 ] à vista no cartão: Desconto de 5%
[ 3 ] em até 2x no cartão: Preço normal 
[ 4 ] 3x ou mais no cartão: Juros de 20%
\nQue opção você deseja: \n"""))

if modo == 1:
    preco = preco - (preco * 0.1)
    print(f"O valor total ficará R${preco} reais.")
elif modo == 2:
    preco = preco - (preco * 0.05)
    print(f"O valor total ficará R${preco} reais.")
elif modo == 3:
    print(f"O valor total ficará de R${preco} reais")
elif modo == 4:
    preco = print(f"O valor total ficará R${preco + preco * 0.2} reais.")







