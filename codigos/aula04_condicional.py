entrada = input("Digite sua idade: ") 

idade = int(entrada)

print("Sua idade é ", idade)

# SE a idade for maior ou igual a 18 anos, ENTÃO:
#   é maior de idade

# 18 19 20 21 22 

if idade >= 18:
    print('é maior de idade')
else:
    print("De menor")
# aposentada: 65 anos ou mais.

if idade > 65:
    print("você é aposentado")
else:
    print("Não é aposentado")
    
if idade == 65:
    print("é momento de aposentar")