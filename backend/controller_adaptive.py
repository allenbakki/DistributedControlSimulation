import socket
import time

HOST = "127.0.0.1"
PORT = 9000

gain = 1.0
target = 50

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    error = target - gain
    gain += 0.05 * error

    s.send(str(gain).encode())
    speed = float(s.recv(1024).decode())

    print("Adaptive Speed:", speed)
    time.sleep(0.1)
