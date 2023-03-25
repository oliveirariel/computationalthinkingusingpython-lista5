ano = int(input("Digite um ano entre 1000 e 2999: "))

if ano < 1000 or ano > 2999:
    print("Ano inválido. Digite um ano entre 1000 e 2999.")
else:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print("O ano é bissexto.")
    else:
        print("O ano não é bissexto.")
