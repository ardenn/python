import unittest
import hello


class HelloTest(unittest.TestCase):

    def test_can_say_hello_to_you_guy(self):
        self.assertEqual(hello.say_hello("Chiamaka"), "Hello, Chiamaka")
if __name__ == "__main__":
    unittest.main()
