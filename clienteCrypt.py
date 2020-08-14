from socket import *
from Crypto.Cipher import AES
chave = "OIESSAEHASENHAOK"
aes = AES.new(chave, AES.MODE_ECB)

servidor = "127.0.0.1"
porta = 60005

while True:
    conexao = socket(AF_INET, SOCK_STREAM)
    conexao.connect((servidor, porta))
    while True:
        texto_claro = bytes(input("Digite uma mensagem: "), 'utf-8')
        while len(texto_claro) % 16 > 0:     
            texto_claro += b"."
            print(texto_claro)
        texto_cifrado = aes.encrypt(texto_claro)
        conexao.send(texto_cifrado)
        resposta = conexao.recv(1024)
        print("Texto Encriptado: ", str(resposta))
        print("Texto claro: ", str(aes.decrypt(resposta)))
    conexao.close()