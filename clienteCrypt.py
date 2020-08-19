from socket import socket, AF_INET, SOCK_STREAM
from Crypto.Cipher import AES
key = "OIESSAEHASENHAOK"
nkey = len(key)
aes = AES.new(key, AES.MODE_ECB)

server = input('Server ID: ')
port = int(input('Server port: '))

while True:
    c = socket(AF_INET, SOCK_STREAM)
    c.connect((server, port))
    while True:
        m = bytes(input("send a message: "), 'utf-8')
        while len(m) % nkey > 0:     
            m += b"&"
        m_crypt = aes.encrypt(m)
        c.send(m_crypt)
        r = c.recv(1024)
        print("received: ", aes.decrypt(r).decode().replace('&',''))
    c.close()