import unittest
from pyworkerqueue import Worker


def print_function(args):
    print(args)


def both_way(args):
    return args


def double_int(args):
    return int(2 * args)


class TestWorker(unittest.TestCase):
    def test_one_way(self):
        with Worker(processes=2, initializer=print_function, bidirectional=False) as w:
            w.put(1)
            w.put("two")
            w.put({"three": 3})
            w.put([4])

    def test_both_way(self):
        with Worker(processes=1, initializer=both_way, bidirectional=True) as w:
            w.put(1)
            self.assertEqual(w.get(), 1)
            w.put("two")
            self.assertEqual(w.get(), "two")
            w.put({"three": 3})
            self.assertEqual(w.get(), {"three": 3})
            w.put([4])
            self.assertEqual(w.get(), [4])

    def test_change_function(self):
        with Worker(processes=1, initializer=both_way, bidirectional=True) as w:
            w.put(1)
            self.assertEqual(w.get(), 1)
            w.function = double_int
            w.put(1)
            self.assertEqual(w.get(), 2)

    def test_bidirectional_error(self):
        with self.assertRaises(ValueError):
            with Worker(processes=1, initializer=both_way, bidirectional=False) as w:
                w.get()
