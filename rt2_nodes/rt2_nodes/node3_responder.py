import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class Responder(Node):
    def __init__(self):
        super().__init__('rt2_responder')
        self.sub = self.create_subscription(
            Int32, '/palindrome_result', self.callback, 10)
        self.pub = self.create_publisher(String, '/palindrome_reply', 10)

    def callback(self, msg: Int32):
        reply = String()
        reply.data = 'Yes' if msg.data == 1 else 'No'
        self.pub.publish(reply)
        self.get_logger().info(f'Received {msg.data} -> {reply.data}')


def main(args=None):
    rclpy.init(args=args)
    node = Responder()
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
