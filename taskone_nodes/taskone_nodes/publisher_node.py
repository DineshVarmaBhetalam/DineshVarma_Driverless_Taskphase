import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')
        self.publisher_ = self.create_publisher(TaskOne, '/taskone', 10)

    def publish_values(self, ang_vel: float, radius: float):
        msg = TaskOne()
        msg.ang_vel = ang_vel
        msg.radius = radius
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Published: ang_vel={ang_vel} rad/s, radius={radius} m')


def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()
    try:
        while rclpy.ok():
            try:
                ang_vel = float(input('Enter angular velocity (rad/s): '))
                radius = float(input('Enter wheel radius (m): '))
            except ValueError:
                print('Invalid input. Please enter numbers only.')
                continue
            node.publish_values(ang_vel, radius)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
