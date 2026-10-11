import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class TaskOneSubscriber(Node):
    def __init__(self):
        super().__init__('taskone_subscriber')
        self.subscription = self.create_subscription(
            TaskOne, '/taskone', self.listener_callback, 10)

    def listener_callback(self, msg: TaskOne):
        speed = msg.ang_vel * msg.radius  # v = ω · r
        self.get_logger().info(
            f'ang_vel={msg.ang_vel:.2f} rad/s, radius={msg.radius:.2f} m '
            f'-> longitudinal speed = {speed:.3f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = TaskOneSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
