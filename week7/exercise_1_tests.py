import unittest
from LinkedList import LinkedList


class UnitTests(unittest.TestCase):
    def test_contains_TF(self):
        ll = LinkedList()
        ll.add("head")
        ll.add("node")
        self.assertTrue(ll.contains("head"))
        self.assertFalse(ll.contains("tails"))
