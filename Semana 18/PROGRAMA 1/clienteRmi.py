import Pyro4

uri = "PYRO:obj_1234567890@localhost:50000"  # Atualize com a URI correta
server = Pyro4.Proxy(uri)

message = input("Digite a mensagem a ser invertida: ")

inverted_message = server.invert_string(message)

print("Mensagem invertida:", inverted_message)