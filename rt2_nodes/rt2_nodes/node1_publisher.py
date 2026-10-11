import threading
import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('rt2_publisher')
        self.publisher_ = self.create_publisher(RT2String, '/rt2_string', 10)
        self.current = None
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        if self.current is None:
            return
        msg = RT2String()
        msg.data = self.current
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')


def read_input(node):
    # Runs in a background thread so input() doesn't block publishing
    while rclpy.ok():
        try:
            text = input('Enter a string (publishes continuously until you enter a new one): ').strip()
        except EOFError:
            break
        if text:
            node.current = text


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    threading.Thread(target=read_input, args=(node,), daemon=True).start()
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
