import Pyro4

@Pyro4.expose
class Calculator(object):
def add(self, num1, num2):
return num1 + num2

daemon = Pyro4.Daemon()
uri = daemon.register(Calculator)
print("Ready. Object uri =", uri)
daemon.requestLoop()