import socket

host="127.0.0.1"

for p in range(1,1025):
    s=socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((host,p));print(f"Porta {p} aberta")
    except:
        pass
    s.close()
