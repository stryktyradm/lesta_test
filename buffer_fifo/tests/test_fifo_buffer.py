import unittest


class FIFOBufferTest(unittest.TestCase):
    def setUp(self):
        self.buffer = None

    def test_add_and_remove_one_item(self):
        q = self.buffer()
        q.push(1)
        self.assertEqual(q.pop(), 1)

    def test_many_add_and_remove_one_item(self):
        q = self.buffer(1000)
        for i in range(1000):
            q.push(i)
        self.assertEqual(q.pop(), 0)

    def test_many_add_and_remove_items(self):
        q = self.buffer(1000)
        for i in range(1000):
            q.push(i)
        for i in range(1000):
            self.assertEqual(q.pop(), i)

    def test_peek_items(self):
        q = self.buffer(3)
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(q.peek(), 1)

    def test_empty_buffer(self):
        q = self.buffer()
        self.assertEqual(q.is_empty(), True)

    def test_full_buffer(self):
        q = self.buffer(1)
        q.push(1)
        self.assertEqual(q.is_full(), True)

    def test_pop_empty_buffer(self):
        q = self.buffer()
        with self.assertRaises(Exception):
            q.pop()

    def test_peek_empty_buffer(self):
        q = self.buffer()
        self.assertEqual(q.peek(), None)

    def test_push_full_buffer(self):
        q = self.buffer(1)
        q.push(1)
        with self.assertRaises(Exception):
            q.push(2)
