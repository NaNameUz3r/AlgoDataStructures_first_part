from dynamic_array import DynArray
import unittest


class DynamicArrayTests(unittest.TestCase):

    def test_create_array(self):
        din_arr = DynArray()
        for i in range(17):
            din_arr.append(i)

    def test_insert_growth(self):
        din_arr = DynArray()
        for i in range(15):
            din_arr.append(i)
        din_arr.insert(15, 1000)
        self.assertEqual(din_arr.count, 16)
        self.assertEqual(din_arr.capacity, 16)
        din_arr.insert(16, 2000)
        self.assertEqual(din_arr.count, 17)
        self.assertEqual(din_arr.capacity, 32)

    def test_insert(self):
        din_arr = DynArray()
        for i in range(1, 15):
            din_arr.append(i)
        din_arr.insert(3, 111)

        self.assertEqual(din_arr[3], 111)
        self.assertEqual(din_arr[4], 4)
        self.assertEqual(din_arr[14], 14)
        self.assertEqual(din_arr.count, 15)
        self.assertEqual(din_arr.capacity, 16)

        din_arr.insert(13, 222)
        din_arr.insert(14, 333)

        self.assertEqual(din_arr.count, 17)
        self.assertEqual(din_arr.capacity, 32)

        self.assertRaises(IndexError, din_arr.insert, -1, 555)
        self.assertRaises(IndexError, din_arr.insert, 18, 444)

    def test_delete(self):
        din_arr = DynArray()
        for i in range(16):
            din_arr.append(i)

        din_arr.delete(0)
        din_arr.delete(14)
        din_arr.delete(4)

        self.assertEqual(din_arr.count, 13)
        self.assertEqual(din_arr.capacity, 16)

        din_arr.capacity = 32
        din_arr.delete(0)

        self.assertEqual(din_arr.capacity, 21)

        self.assertRaises(IndexError, din_arr.delete, -1)
        self.assertRaises(IndexError, din_arr.delete, 13)
