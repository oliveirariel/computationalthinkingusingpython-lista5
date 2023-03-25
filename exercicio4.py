preco = float(input("Qual o preço do livro? "))

if preco <= 10.0:
    desconto = preco * 0.08
elif preco <= 60.0:
    desconto = preco * 0.1
else:
    desconto = preco * 0.2

print("O desconto oferecido é de R$", round(desconto, 2))
