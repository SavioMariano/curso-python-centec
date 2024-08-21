print("Informe o meio de conversão:\n")

print("C - de celsius para fahrenheit")
print("F - de fahrenheit para celsius\n")

escolha = input("Escolha: ")

if escolha == "c" or escolha == "C":
    c = input("\nDigite temperatura em celsius: ")
    conversor = float(c) * 1.8 + 32
    print("\nA temperatura é:", conversor, "em Fahrenheit" )
elif escolha == "f" or escolha == "F":
    f = input("\nDigite temperatura em Fahrenheit:")
    conversor = (float(f) - 32) / 1.8
    print("\nA temperatura é:", conversor, "em Celsius")
else:
    print("valor invalido")
