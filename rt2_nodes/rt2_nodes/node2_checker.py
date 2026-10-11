import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
from rt2_interfaces.msg import RT2String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('rt2_checker')
        self.sub_string = self.create_subscription(
            RT2String, '/rt2_string', self.string_callback, 10)
        self.pub_result = self.create_publisher(Int32, '/palindrome_result', 10)
        self.sub_reply = self.create_subscription(
            String, '/palindrome_reply', self.reply_callback, 10)

    def string_callback(self, msg: RT2String):
        text = msg.data
        is_palindrome = text == text[::-1]
        out = Int32()
        out.data = 1 if is_palindrome else 0
        self.pub_result.publish(out)
        self.get_logger().info(f'Received "{text}" -> sent {out.data} to Node 3')

    def reply_callback(self, msg: String):
        self.get_logger().info(f'Reply from Node 3: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
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
