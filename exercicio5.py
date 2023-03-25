peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

print("O IMC é de:", round(imc, 2))

if imc < 18.5:
    print("Situação: Abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Situação: Peso normal.")
elif imc >= 25 and imc < 30:
    print("Situação: Sobrepeso.")
elif imc >= 30 and imc < 35:
    print("Situação: Obesidade grau I.")
elif imc >= 35 and imc < 40:
    print("Situação: Obesidade grau II.")
else:
    print("Situação: Obesidade grau III.") 
