import socket

servidor_ip = '127.0.0.1' 
porta = 8080 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    
    servidor.bind((servidor_ip, porta))
    servidor.listen()
    print('Servidor iniciado...')
    conexao, endereco = servidor.accept()
    
    with conexao:
        print('Conexão estabelecida por', endereco)
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
        print('Mensagem recebida:', dados.decode())