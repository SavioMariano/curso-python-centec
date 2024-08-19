peso = input("Informe sua peso em (kg): \n> ")
peso = float(peso)

altura = input("Informe sua altura:\n> ")
altura = float(altura)

print("\n::::::CALCULANDO IMC::::::\n")

imc = peso / (altura ** 2)

print("Seu IMC é:\n> ", imc, "\n\n")

if imc <= 18.5:
    print("Abaixo do peso")
    
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
    
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
    
elif imc >= 30 and imc < 35:
    print("Obesidade Grau I")

elif imc >= 35 and imc < 40:
    print("Obseidade Grau II")
    
elif imc >= 40:
    print("Obesidade Grau III")
