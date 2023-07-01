import Pyro4

@Pyro4.expose
class Stringverter(object):
def invert(self, message):
return message[::-1]

daemon = Pyro4.Daemon()
uri = daemon.register(StringInverter)
print("Ready. Object uri =", uri)
daemon.requestLoop()