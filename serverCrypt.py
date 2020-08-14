from socket import *
from Crypto.Cipher import AES
chave = "OIESSAEHASENHAOK"
aes = AES.new(chave, AES.MODE_ECB)

servidor = "127.0.0.1"
porta = 60005

conexao = socket(AF_INET, SOCK_STREAM)
conexao.bind((servidor, porta))
conexao.listen(2)
print("Esperando Usuario...")
while True:
    con, cliente = conexao.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = con.recv(1024)
        print("Texto Encriptado: ", msg_recebida)
        print("Texto claro: ", aes.decrypt(msg_recebida))
        msg_enviada = bytes(input("Digite uma mensagem: "), 'utf-8')
        while len(msg_enviada) % 16 > 0:
            msg_enviada += b"."
            print(msg_enviada)
        msg_cifrado = aes.encrypt(msg_enviada)
        con.send(msg_cifrado)
    con.close()