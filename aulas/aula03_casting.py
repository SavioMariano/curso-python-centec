#Exemplos de Casting.

texto = "5.99"

valor = "8.3"

#Exemplificando conceitos de casting 

numero = float(texto)
numero2 = float(valor)
print(  numero + numero2 )

int = 25
int2 = 50

novo_valor = float(int) 
novo_valor2 = float(int2)

print(novo_valor + novo_valor2)

#transformando tpo float para inteiro
valor = int(8.3)
#Ao transformar um float em inteiro NÃO arredonda o número, somente pega a parte inteira do valor.
print(valor)

#Transformando tipo float para String 
valor2 = str(2.5)
print(valor2)

print(f"Minha idade é {str(17)}") #O str(17) indica que o 17 é uma String
