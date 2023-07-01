import Pyro4

uri = input("Digite o URI do servidor: ")
calculator = Pyro4.Proxy(uri)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

result = calculator.add(num1, num2)

print("Resultado da soma:", result)