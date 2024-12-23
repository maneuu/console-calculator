from art import logo
import os
import math

# Função para limpar o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Operações básicas
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Operação de potenciação
def power(n1, n2):
    return n1 ** n2

# Operação de raiz quadrada
def square_root(n1):
    return math.sqrt(n1)

# Dicionário com as operações
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "**": square_root,
}

# Função principal da calculadora
def calculator():
    clear_terminal()
    print(logo)
    print("=" * 40)
    print("💻 Bem-vindo à Calculadora Interativa! 💻")
    print("=" * 40)
    
    num1 = float(input("\n🔢 Qual o primeiro número?: "))
    print("\n🧮 Operações disponíveis:")
    for symbol in operations:
        print(f"   {symbol}")
    print("=" * 40)
    
    while True:
        while True:
            operation_symbol = input("\n✨ Escolha uma operação: ")
            if operation_symbol in operations:
                break
            print("❌ Por favor, escolha uma operação válida.")
        
        if operation_symbol == "**":
            if num1 < 0:
                print('Erro: Não é possível calcular a raiz quadrada de um número negativo.')
                while True:
                    num1 = float(input("\n🔢 Digite um número maior ou igual a 0: "))
                    if num1 >= 0:
                        break
            answer = operations[operation_symbol](num1)
            print(f"\n📐 Resultado: √{num1} = {answer}")
        else:
            num2 = float(input("\n🔢 Qual o próximo número?: "))
            if operation_symbol == "/" and num2 == 0:
                print("\n❌ Erro: Divisão por zero não é permitida.")
                while True:
                    num2 = float(input("\n🔢 Digite um número diferente de 0: "))
                    if num2 != 0:
                        break
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"\n📐 Resultado: {num1} {operation_symbol} {num2} = {answer}")
        
        print("=" * 40)
        while True:
            repeat = input(f"🔄 Deseja continuar com {answer}? (Digite 's' para sim, 'n' para nova operação): ").lower()
            if repeat in ['s', 'n']:
                break
            print("❌ Resposta inválida. Por favor, digite 's' ou 'n'.")
        
        if repeat == "n":
            clear_terminal()
            calculator()
            break
        num1 = answer

# Inicia a calculadora
calculator()
