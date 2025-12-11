# **Distributed Control Simulation (Python + Socket Programming + React)**

A complete simulation of a distributed control architecture involving a DC motor plant, multiple controllers (PID & Adaptive), and a real-time React dashboard. Built using Python sockets, multithreading, Flask REST API, and ReactJS.

---

## **👥 Team Members**

* **Reshma Dudekula**
* **Raja Sekhar Devu**
* **Shiv Mohith Devana**

---

## **📌 Introduction**

Modern engineering systems—such as autonomous vehicles, robotics, and industrial automation—depend on multiple distributed controllers operating simultaneously. These controllers must coordinate over a communication network, respond in real-time, and maintain system stability. Testing this on real hardware is expensive and risky.

This project simulates a complete distributed control system using **socket programming**, allowing multiple controllers to interact with a DC motor “plant” in real-time.

### **Problems Addressed**

* Simulating a physical plant receiving multiple control inputs
* Enabling controllers to exchange data in real-time
* Visualizing plant dynamics and controller outputs
* Comparing PID and Adaptive controllers
* Avoiding race conditions and managing concurrency

---

## **🎯 Project Objectives**

### **Core Functionalities**

1. Develop a socket-based distributed control simulator
2. Simulate a DC motor plant responding to controller inputs
3. Implement both PID and Adaptive controllers
4. Maintain real-time bidirectional TCP communication
5. Create a React dashboard to visualize:

   * Current speed
   * Target speed
   * Controller inputs
   * Speed vs Time graph
6. Support multiple controllers simultaneously

### **Additional Features**

* Thread locks to prevent inconsistent state
* Optimized sampling intervals for stability
* Modular design for future controllers/network effects
* Full integration across server, controllers, and frontend

---

## **📊 Comparison With Proposal**

All proposed features have been successfully implemented:

✔ Socket-based client–server communication
✔ Multithreaded plant server
✔ PID Controller
✔ Adaptive Controller
✔ Real-time plant state updates
✔ React dashboard with REST API
✔ Speed–Time visualization
✔ Controller input logs

The project fully meets the objectives from the original proposal.

---

## **⚠️ Technical Challenges & Solutions**

### **1. Real-Time Bidirectional Communication**

**Challenge:** Controllers require continuous command + feedback exchange
**Solution:**

* TCP server on port **9000**
* Multithreading for parallel controller connections
* Flask API (port 5000) for frontend

---

### **2. Inconsistent State due to Concurrent Writes**

**Challenge:** Multiple controllers writing to the plant state caused race conditions
**Solution:**

* Implemented `threading.Lock()` to enforce atomic updates

---

### **3. Unstable Initial Controller Outputs**

**Challenge:** PID produced unstable/infinite values initially
**Solution:**

* Added smoothing
* Adjusted update frequency to 100ms
* Tuned gains and error rules

---

### **4. Frontend Performance (UI Flickering)**

**Challenge:** Too many updates caused lag and flicker
**Solution:**

* Limited updates to every 500ms
* Buffered history
* Improved graph rendering logic

---

## **🗂 Folder Structure**

```
/project
│
├── plant_server.py
├── controller_pid.py
├── controller_adaptive.py
└── frontend-react/
```

---

## **🚀 Getting Started**

### **1. Clone the Repository**

```bash
git clone https://github.com/allenbakki/DistributedControlSimulation
cd DistributedControlSimulation
```

---

## **📡 Start the Plant Server**

### Install dependencies:

```bash
pip install flask flask-cors
```

### Run the server:

```bash
python plant_server.py
```

This starts:

* **TCP Socket Server** → port **9000**
* **Flask REST API** → port **5000**

These maintain the plant state (speed, target, controller inputs).

---

## **🎛️ Run the Controllers**

### **Run PID Controller**

```bash
python controller_pid.py
```

### **Run Adaptive Controller**

```bash
python controller_adaptive.py
```

Both controllers continuously send control inputs to the plant while receiving real-time feedback.

---

## **🖥️ Start the React Frontend**

```bash
cd frontend-react
npm install
npm start
```

Frontend available at:

```
http://localhost:3000
```

Displays:

* Live plant speed
* Target speed
* Controller inputs
* Speed vs Time line graph

---

## **📘 Overview**

This project simulates:

* A DC motor plant
* Multiple distributed controllers
* Real-time network communication
* Concurrency & stability challenges
* Visual monitoring with a modern React dashboard

Technologies used:

* **Python Sockets**
* **Multithreading**
* **Flask API**
* **ReactJS**
