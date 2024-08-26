array = [-1,-15, -10, -14, -13, -11, -2, -12949]
maior = 0
menor = float('inf')

for elemento in array:
    if maior < elemento or maior == 0 and maior > elemento:
        maior = elemento
    if menor > elemento:
        menor = elemento
    
print("Maior número:",maior)
print("Menor número:",menor)