import socket
import time

HOST = "127.0.0.1"
PORT = 9000

Kp = 2
Ki = 0.1
Kd = 0.01

target = 50
integral = 0
prev_error = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    error = target - prev_error
    integral += error
    derivative = error - prev_error

    control = Kp*error + Ki*integral + Kd*derivative

    s.send(str(control).encode())
    speed = float(s.recv(1024).decode())

    print("Speed:", speed)

    prev_error = speed
    time.sleep(0.1)
