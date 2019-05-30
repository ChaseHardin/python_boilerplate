import unittest

from src.hello_world import greeting


class TestHelloWorld(unittest.TestCase):
    def test_hello_world_says_greeting(self):
        self.assertEqual(greeting(), "greeting")
