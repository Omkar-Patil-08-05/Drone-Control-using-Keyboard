import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import tty
import termios

class Controller(Node):

    def __init__(self):
        super().__init__('controller')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def move(self, linear=0.0, angular=0.0):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        self.pub.publish(msg)

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def main():
    rclpy.init()
    node = Controller()

    print("Controls: W/S/A/D + X(stop)")

    try:
        while True:
            key = get_key()

            if key == 'w':
                node.move(0.3, 0.0)
            elif key == 's':
                node.move(-0.3, 0.0)
            elif key == 'a':
                node.move(0.0, 0.8)
            elif key == 'd':
                node.move(0.0, -0.8)
            elif key == 'x':
                node.move(0.0, 0.0)

    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__ == '__main__':
    main()