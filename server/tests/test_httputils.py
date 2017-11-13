import unittest

from wydra import httputils


class TestHttputils(unittest.TestCase):
    def test_extract_path(self):
        self.assertEqual(httputils.extract_path('/path/123'), ('path', '123'))


if __name__ == '__main__':
    unittest.main()
