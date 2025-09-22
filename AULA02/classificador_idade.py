idade = int(input("Digite sua idade: "))
if idade < 0 or idade > 110:
    print("Idade inválida")
elif idade < 12:
    print("criança")
elif idade < 18:
    print("adolescente")
elif idade < 65:
    print("adulto")
else:
    print("idoso")