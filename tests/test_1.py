
import unittest

import platos


class MyTestCase(unittest.TestCase):

    def test_loads(self):
        obj = platos.loads("* hello\n  world")
        assert obj == ["hello", "world"]

    def test_dumps(self):
        text = platos.dumps("hello")
        assert text == "hello"
        text = platos.dumps(["hello", "world"])
        assert text == "* hello\n  world"
