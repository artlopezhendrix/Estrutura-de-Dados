numero = int(input("Digite um número inteiro positivo para a contagem regressiva: "))

print(f"\nContagem regressiva a partir de {numero}:")

while numero >= 0:
    print(numero)
    numero -= 1 

print("Acabou!")