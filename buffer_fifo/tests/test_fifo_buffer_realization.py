import unittest
from test_fifo_buffer import FIFOBufferTest
from buffer_fifo.linked_fifo import LinkedBufferFIFO
from buffer_fifo.array_fifo import ArrayBufferFIFO


class TestLinkedBufferFIFO(FIFOBufferTest):
    def setUp(self):
        self.buffer = LinkedBufferFIFO


class TestArrayBufferFIFO(FIFOBufferTest):
    def setUp(self):
        self.buffer = ArrayBufferFIFO


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TestLinkedBufferFIFO))
    suite.addTest(loader.loadTestsFromTestCase(TestArrayBufferFIFO))
    return suite


if __name__ == "__main__":
    unittest.main(testLoader=load_tests)
