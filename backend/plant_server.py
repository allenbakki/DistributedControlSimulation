import socket
import threading
import time
from flask import Flask, jsonify
from flask_cors import CORS

# ------------------------------
# Plant State
# ------------------------------
plant_state = {
    "speed": 0.0,
    "target": 50.0,
    "timestamp": time.time(),
    "controller_inputs": []
}

lock = threading.Lock()

# ------------------------------
# TCP SERVER (for controllers)
# ------------------------------
def handle_client(conn, addr):
    global plant_state

    print(f"[CONNECTED] Controller connected: {addr}")

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            controller_value = float(data)

            with lock:
                plant_state["controller_inputs"].append(controller_value)
                # Motor update: simple model
                plant_state["speed"] += 0.1 * (controller_value - plant_state["speed"])
                plant_state["timestamp"] = time.time()

            conn.send(str(plant_state["speed"]).encode())

        except:
            break

    conn.close()
    print("[DISCONNECTED] Controller closed")


def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9000))
    server.listen()

    print("[PLANT] Listening on port 9000...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

# ------------------------------
# HTTP Server for React UI
# ------------------------------

app = Flask(__name__)
# In Flask
CORS(app)

@app.get("/state")
def get_state():
    with lock:
        return jsonify(plant_state)

def start_http():
    app.run(port=5000)

# ------------------------------
# Main
# ------------------------------
if __name__ == "__main__":
    threading.Thread(target=tcp_server).start()
    threading.Thread(target=start_http).start()
