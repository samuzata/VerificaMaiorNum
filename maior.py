num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")

def verificaMaiorNumero(x, y, z):
    if x > y and x > z:
        print ("O maior número é " + x)
    elif y > x and y > z:
        print ("O maior número é " + y)
    elif z > x and z > y:
        print ("O maior número é " + z)
        
    else:
        print("Todos os números são iguais")
    


print(f"Os números digitados foram {num1}, {num2} e {num3}")
verificaMaiorNumero(num1, num2, num3)