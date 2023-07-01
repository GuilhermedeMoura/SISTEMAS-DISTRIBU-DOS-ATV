import Pyro4

uri = "PYRO:obj_1234567890@localhost:50000"  # Atualize com a URI correta
server = Pyro4.Proxy(uri)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

result = server.sum_numbers(num1, num2)

print("Resultado da soma:", result)