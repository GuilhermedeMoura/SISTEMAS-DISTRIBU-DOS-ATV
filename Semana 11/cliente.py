
import socket

servidor_ip = '127.0.0.1'
porta = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexao:

    conexao.connect((servidor_ip, porta))
    mensagem = input('Digite a mensagem a ser enviada: ')
    conexao.sendall(mensagem.encode())