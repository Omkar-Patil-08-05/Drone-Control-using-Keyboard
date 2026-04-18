from pymavlink import mavutil
import time
import sys
import tty
import termios
import select

# Connect
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
master.wait_heartbeat()
print("✅ Connected")

def send_velocity(vx, vy, vz):
    master.mav.set_position_target_local_ned_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111000111,
        0, 0, 0,
        vx, vy, vz,
        0, 0, 0,
        0, 0
    )

#  NON-BLOCKING KEY INPUT
def get_key_nonblocking():
    dr, dw, de = select.select([sys.stdin], [], [], 0)
    if dr:
        return sys.stdin.read(1)
    return None

# Setup terminal
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setcbreak(fd)

#  Initial setpoints BEFORE OFFBOARD
print("🚀 Sending initial setpoints...")
for _ in range(200):
    send_velocity(0, 0, -0.2)
    time.sleep(0.02)

#  Set OFFBOARD
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    6
)

time.sleep(1)

#  Arm
master.arducopter_arm()
master.motors_armed_wait()

print("✅ Armed + OFFBOARD ACTIVE")

print("🎮 Controls:")
print("W/S → forward/back")
print("A/D → left/right")
print("U → UP | J → DOWN")
print("X → stop")

#  CONTROL VARIABLES
vx, vy, vz = 0, 0, -0.2

try:
    while True:

        #  read key WITHOUT blocking
        key = get_key_nonblocking()

        if key == 'w':
            vx = 1
        elif key == 's':
            vx = -1
        elif key == 'a':
            vy = -1
        elif key == 'd':
            vy = 1
        elif key == 'u':
            vz = -1
        elif key == 'j':
            vz = 1
        elif key == 'x':
            vx, vy, vz = 0, 0, 0

        # ALWAYS send (CRITICAL)
        send_velocity(vx, vy, vz)

        time.sleep(0.05)   # ~20Hz

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)