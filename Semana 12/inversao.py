import socket

grupo_multicast = ('224.3.29.71', 10000)

socket_multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = input('Digite a mensagem a ser invertida: ')
socket_multicast.sendto(mensagem.encode('utf-8'), grupo_multicast)

dados, servidor = socket_multicast.recvfrom(1024)
print('Mensagem invertida:', dados.decode('utf-8'))