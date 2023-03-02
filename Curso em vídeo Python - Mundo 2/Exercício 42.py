#Exercício 42
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

reta1 = float(input("Informe o comprimento da primeira reta: "))
reta2 = float(input("Informe o comprimento da segunda reta: "))
reta3 = float(input("Informe o comprimento da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f"Sim! Esses valores podem formar um triângulo.")

    if reta1 == reta2 and reta1 == reta3:
        print("Triângulo EQUILÁTERO")
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print("Triângulo ISÓSCELES")
    elif reta1 != reta2 and reta1 != reta3:
        print("Triângulo ESCALENO")
        
else:
    print(f"Esses valores não formar um triângulo.")



