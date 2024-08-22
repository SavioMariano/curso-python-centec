
multiplo = int(input("Digite o multiplo: "))
valores = int(input("Digite quantas vezes quer multiplicar: "))
valor = 0

for multiplicar in range(1, (valores + 1) , 1):
        valor += multiplo
    
        print("O multiplo de", multiplo, "é", valor)  

