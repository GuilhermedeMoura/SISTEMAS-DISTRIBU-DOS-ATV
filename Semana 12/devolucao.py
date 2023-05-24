import socket
import struct

grupo_multicast = '224.3.29.71'
endereco_servidor = ('', 10000)

socket_multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_multicast.bind(endereco_servidor)

grupo = socket.inet_aton(grupo_multicast)
mreq = struct.pack('4sL', grupo, socket.INADDR_ANY)
socket_multicast.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    
    print('\nAguardando receber mensagem...')
    dados, endereco = socket_multicast.recvfrom(1024)
    print('Recebidos {} bytes de {}.'.format(len(dados), endereco))

    mensagem = dados.decode('utf-8')
    mensagem_invertida = mensagem[::-1]

    print('Enviando mensagem invertida de volta para', endereco)
    socket_multicast.sendto(mensagem_invertida.encode('utf-8'), endereco)