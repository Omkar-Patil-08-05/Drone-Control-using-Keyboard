# 🚁 Drone Control using Keyboard (PX4 + MAVLink)

## 📌 Project Overview

This project demonstrates real-time drone control using keyboard inputs in PX4 SITL simulation (jMAVSim).

The drone is controlled in **OFFBOARD mode** using MAVLink velocity commands.

---

## ⚠️ IMPORTANT (READ FIRST)

* Do NOT install random PX4 repos
* Use the official PX4 repository only
* OFFBOARD mode must be enabled manually

---

# 🛠️ INSTALLATION (STEP-BY-STEP)

## 🔹 1. Install PX4 (Correct Way)

```bash
cd ~
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
cd PX4-Autopilot
bash ./Tools/setup/ubuntu.sh
```

👉 After installation, restart terminal or run:

```bash
source ~/.bashrc
```

---

## 🔹 2. Install Python Dependencies

```bash
pip3 install pymavlink
```

---

# ▶️ HOW TO RUN

## 🔹 Step 1: Start PX4 Simulation

```bash
cd ~/PX4-Autopilot
make px4_sitl jmavsim
```

---

## 🔹 Step 2: Run Controller Script

Open new terminal:

```bash
python3 control.py
```

You should see:

```
Connected
Sending initial setpoints...
```

---

## 🔹 Step 3: Enable OFFBOARD Mode (MANDATORY)

In PX4 terminal (pxh>):

```bash
commander arm
commander mode offboard
```

---

# 🎮 CONTROLS

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

# 🚨 COMMON ISSUES (VERY IMPORTANT)

## ❌ Drone not moving

👉 Cause: Not in OFFBOARD mode

✔ Fix:

```bash
commander mode offboard
```

---

## ❌ GPS warning

```
Preflight: GPS fix too low
```

✔ Ignore (normal in simulation)

---

## ❌ Script crashes with termios error

👉 Cause: Running script in background

✔ Fix:

```bash
python3 control.py
```

(run in foreground only)

---

# 🧠 SYSTEM WORKFLOW

1. PX4 starts simulation
2. Python script sends velocity setpoints
3. PX4 switches to OFFBOARD mode
4. Drone follows commands

---

# 📌 FEATURES

* Real-time keyboard control
* 3D movement (including altitude)
* MAVLink-based OFFBOARD control
* Works with PX4 SITL

---