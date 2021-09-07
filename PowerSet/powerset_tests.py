import random
import unittest
from power_set import PowerSet


class PowerSetTests(unittest.TestCase):

    def test_put_and_remove(self):
        ps = PowerSet()
        ps.put("Hello")
        self.assertEqual(ps.set[0], "Hello")
        self.assertEqual(ps.get("Hello"), True)
        self.assertEqual(ps.put("Hello"), None)
        self.assertEqual(ps.set[0], "Hello")
        self.assertEqual(ps.get("Hello"), True)
        self.assertEqual(ps.size(), 1)
        self.assertEqual(ps.remove("Hello"), True)
        self.assertEqual(ps.set, [])

    def test_intersection(self):
        ps1 = PowerSet()
        ps1.set = [1, 2, 3]

        ps2 = PowerSet()
        ps2.set = [2, 3, 4]

        ps3 = PowerSet()
        ps3.set = [5, 6, 7]

        self.assertEqual(ps1.intersection(ps2).set, [2, 3])
        self.assertEqual(ps1.intersection(ps3).set, [])

    def test_union(self):
        ps1 = PowerSet()
        ps1.set = [1, 2, 3]

        ps2 = PowerSet()
        ps2.set = [2, 3, 4]

        ps3 = PowerSet()

        self.assertEqual(ps1.union(ps2).set, [1, 2, 3, 4])
        self.assertEqual(ps1.union(ps3).set, ps1.set)

    def test_diff(self):
        ps1 = PowerSet()
        ps1.set = [1, 2, 3]

        ps2 = PowerSet()
        ps2.set = [2, 3, 4]

        ps3 = PowerSet()
        ps3.set = [2, 3, 4]

        self.assertEqual(ps1.difference(ps2).set, [1, 4])
        self.assertEqual(ps2.difference(ps3).set, [])

    def test_subset(self):
        ps1 = PowerSet()
        ps1.set = [1, 2, 3]

        ps2 = PowerSet()
        ps2.set = [2, 3]

        ps3 = PowerSet()
        ps3.set = [1, 2, 3]

        ps4 = PowerSet()
        ps4.set = [3, 4]

        self.assertEqual(ps1.issubset(ps2), True)
        self.assertEqual(ps1.issubset(ps3), True)
        self.assertEqual(ps1.issubset(ps4), False)

    def test_speed(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        for i in range(1, 10000):
            ps1.put(random.randint(1, 99999999))
        for i in range(1, 20000):
            ps2.put(random.randint(1, 99999999))

        ps3 = PowerSet()
        ps3.set = [1, 3, 9]

        print(ps1.issubset(ps2))

