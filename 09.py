# Exercício 9: Calculadora simples
# Use match-case para escolher a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

match op:
    case "+":
        ...
    case "-":
        ...
    case "*":
        ...
    case "/":
        ...
    case _:
        print("Operação inválida")
