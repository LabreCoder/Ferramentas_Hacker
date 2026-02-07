import socket

host="bancocn.com" # esse é um site que foi montado pelo  site da Solyd para ser usado em testes de segurança, não é ilegal fazer varreduras nesse site, mas é ilegal fazer varreduras em sites sem autorização, então use esse código apenas para fins educacionais e teste somente em sites que você tem autorização para testar.

for p in range(1,1025):
    s=socket.socket()
    s.settimeout(0.01)
    try:
        s.connect((host,p));print(f"{host} -> Porta {p} aberta")
    except:
        pass
    s.close()
