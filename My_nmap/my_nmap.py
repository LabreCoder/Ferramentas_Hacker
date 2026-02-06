import socket

host="bancocn.com"

for p in range(1,1025):
    s=socket.socket()
    s.settimeout(0.01)
    try:
        s.connect((host,p));print(f"{host} -> Porta {p} aberta")
    except:
        pass
    s.close()
