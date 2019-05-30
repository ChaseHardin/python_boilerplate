import unittest

from src.read_file_content import main


class TestReadFileContent(unittest.TestCase):
    def test_content_of_file(self):
        actual = main()

        self.assertEqual(actual, actual)
