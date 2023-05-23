import socket

HOST = '127.0.0.1'
PORT = 12345

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_cliente.connect((HOST, PORT))

mensagem = 'SEND_MESSAGE:alice:Olá, Alice!'
socket_cliente.sendall(mensagem.encode('utf-8'))

resposta = socket_cliente.recv(1024).decode('utf-8')

partes_resposta = resposta.split(':')
tipo_resposta = partes_resposta[0]
corpo_resposta = partes_resposta[1]

socket_cliente.close()