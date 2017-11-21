import base64
import unittest
import uuid

from wydra import httputils


class TestExtractPath(unittest.TestCase):
    def test_extract_path(self):
        self.assertEqual(httputils.extract_path('/path/123'), ('path', '123'))

    def test_extract_path_empty(self):
        self.assertEqual(httputils.extract_path(''), ('/', ''))

    def test_extract_path_slash(self):
        self.assertEqual(httputils.extract_path('/'), ('/', ''))

    def test_extract_path_random(self):
        s = str(uuid.uuid4())
        self.assertEqual(httputils.extract_path('/' + s), (s, ''))


class TestExtractPassphrase(unittest.TestCase):
    def test_extract_passphrase(self):
        payload = 'Basic ' + base64.b64encode(b':password').decode()
        self.assertEqual(httputils.extract_passphrase(payload), b'password')


if __name__ == '__main__':
    unittest.main()
