import socket

HOST = '127.0.0.1'
PORT = 12345

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_servidor.bind((HOST, PORT))

socket_servidor.listen(5)

while True:

    socket_cliente, endereco_cliente = socket_servidor.accept()

    mensagem = socket_cliente.recv(1024).decode('utf-8')

    partes_mensagem = mensagem.split(':')
    tipo_mensagem = partes_mensagem[0]
    corpo_mensagem = partes_mensagem[1]

    mensagem_resposta = 'Olá, cliente!'
    socket_cliente.sendall(mensagem_resposta.encode('utf-8'))

    socket_cliente.close()

socket_servidor.close()