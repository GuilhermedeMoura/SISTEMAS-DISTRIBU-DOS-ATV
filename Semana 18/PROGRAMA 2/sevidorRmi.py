import Pyro4

@Pyro4.expose
class NumberSumServer:
    def sum_numbers(self, num1, num2):
        return num1 + num2

daemon = Pyro4.Daemon()
uri = daemon.register(NumberSumServer)

print("Servidor RMI iniciado.")
print("URI do objeto remoto:", uri)