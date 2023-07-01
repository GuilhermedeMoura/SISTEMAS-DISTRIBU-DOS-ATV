import Pyro4

uri = input("Digite o URI do servidor: ")
string_inverter = Pyro4.Proxy(uri)

message = input("Digite a mensagem que será invertida: ")
inverted_message = string_inverter.invert(message)

print("Mensagem invertida:", inverted_message)