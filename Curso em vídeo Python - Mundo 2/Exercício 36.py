#Exercício 36
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vlrcasa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o seu salário: "))
anos = int(input("Informe em quantos anos você pretende pagar: "))

prestacao = vlrcasa / (anos * 12)

if prestacao > salario * 0.3:
    print("Empréstimo negado.")
else:
    print("Empréstimo aprovado.")