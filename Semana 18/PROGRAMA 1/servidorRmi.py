import Pyro4

@Pyro4.expose
class StringInverterServer:
    def invert_string(self, string):
        return string[::-1]

daemon = Pyro4.Daemon()
uri = daemon.register(StringInverterServer)

print("Servidor RMI iniciado.")
print("URI do objeto remoto:", uri)

daemon.requestLoop()