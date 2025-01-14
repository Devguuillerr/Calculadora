from funcao import *

while True:
    print("Selecione uma opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    escolha = input("Escolha uma opção (1-5): ")
    
    if escolha == '1':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif escolha == '2':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif escolha == '3':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif escolha == '4':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Não é possível dividir por zero.")
    elif escolha == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
