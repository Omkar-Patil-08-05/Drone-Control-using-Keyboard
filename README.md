# 🚁 Drone Control using Keyboard (PX4 + MAVLink + Gazebo)

## 📌 Project Overview

This project demonstrates **keyboard-based control** of a drone using:

* PX4 SITL (jMAVSim) → **3D drone control**
* MAVLink (pymavlink) → communication
* ROS2 + Gazebo → **2D robot control (extra module)**

---

# ⚠️ IMPORTANT NOTES

* Use **official PX4 repo only**
* OFFBOARD mode must be enabled manually
* Run controller scripts in **foreground (not background)**

---

# 🛠️ INSTALLATION

## 🔹 1. Install PX4 (Correct Way)

```bash
cd ~
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
cd PX4-Autopilot
bash ./Tools/setup/ubuntu.sh
```

After installation:

```bash
source ~/.bashrc
```

---

## 🔹 2. Install Python Dependencies

```bash
pip3 install pymavlink
```

---

# 🚀 PX4 DRONE CONTROL (3D)

## ▶️ Step 1: Start PX4 Simulation

```bash
cd ~/PX4-Autopilot
make px4_sitl jmavsim
```

---

## ▶️ Step 2: Run Controller

Open new terminal:

```bash
python3 px4_control/control.py
```

You should see:

```
Connected
Sending initial setpoints...
```

---

## ▶️ Step 3: Enable OFFBOARD Mode (MANDATORY)

In PX4 terminal (`pxh>`):

```bash
commander arm
commander mode offboard
```

---

## 🎮 Controls

| Key | Action   |
| --- | -------- |
| W   | Forward  |
| S   | Backward |
| A   | Left     |
| D   | Right    |
| U   | Up       |
| J   | Down     |
| X   | Stop     |

---

## 🚨 Common Issues

### ❌ Drone not moving

✔ Fix:

```bash
commander mode offboard
```

---

### ❌ GPS warning

```
Preflight: GPS fix too low
```

✔ Ignore (normal in simulation)

---

### ❌ Script crash (termios error)

✔ Cause: running in background
✔ Fix:

```bash
python3 px4_control/control.py
```

---

# 🤖 GAZEBO ROBOT CONTROL (2D)

## 📌 Description

This module demonstrates **2D movement of a robot** using ROS2 and Gazebo.

---

## ▶️ Step 1: Source ROS2

```bash
source /opt/ros/humble/setup.bash
```

---

## ▶️ Step 2: Set TurtleBot Model

```bash
export TURTLEBOT3_MODEL=burger
```

---

## ▶️ Step 3: Launch Gazebo World

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

---

## ▶️ Step 4: Run Controller

```bash
ros2 run drone_control controller
```

---

## 🎮 Controls

| Key | Action   |
| --- | -------- |
| W   | Forward  |
| S   | Backward |
| A/D | Turn     |
| X   | Stop     |

---

# 🧠 SYSTEM WORKFLOW

### PX4:

1. PX4 starts simulation
2. Python sends velocity commands
3. User enables OFFBOARD mode
4. Drone responds

### Gazebo:

1. Gazebo launches world
2. ROS2 node publishes velocity
3. Robot moves in 2D

---

# 📌 FEATURES

* ✅ Keyboard-based control
* ✅ 3D drone movement (PX4)
* ✅ 2D robot movement (Gazebo)
* ✅ OFFBOARD MAVLink control
* ✅ Real-time response

