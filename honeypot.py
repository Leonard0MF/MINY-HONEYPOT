import socket
import threading
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "connections.log")
PORT = 8080

# Garante que a pasta de logs existe
os.makedirs(LOG_DIR, exist_ok=True)

def log_connection(addr, data):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] Conexão de {addr[0]}:{addr[1]} -> {data.strip()}\n")

def handle_client(conn, addr):
    print(f"[+] Nova conexão de {addr}")
    try:
        data = conn.recv(1024).decode(errors="ignore")
        if data:
            log_connection(addr, data)
        conn.send(b"Obrigado pela conexao!\n")
    except Exception as e:
        print(f"[!] Erro: {e}")
    finally:
        conn.close()

def start_honeypot():
    print(f"[+] Honeypot escutando na porta {PORT}...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", PORT))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_honeypot()
