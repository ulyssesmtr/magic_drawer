import unittest
from magic_drawer import magic_drawer, process_coin_operation

class MagicDrawerTests(unittest.TestCase):

    def test_exercise_value(self):
        """Should return 12"""
        self.assertEqual(magic_drawer([1, -1, 2, 0, 4]), 12)
    
    def test_multiple_zeros(self):
        """Should return 0"""
        self.assertEqual(magic_drawer([0, 0, 0, 0, 0, 0, 0, 0]), 0)
    
    def test_random_valid_array(self):
        """Should return 176"""
        self.assertEqual(magic_drawer([2, -1, 7, 3, -5, 10, -2]), 176)
    
    def test_exception(self):
        """
        When the amount to be retrieved is more than half of what
        is currently at the drawer, an exception should be raised
        """
        self.assertRaises(Exception, magic_drawer, [1, -3, 2, 0, 4])

    def test_single_number_array(self):
        """
        If an array with just one operation is used, 
        the return should be the single value
        """
        self.assertEqual(magic_drawer([2]), 2)

class ProcessCoinOperationTests(unittest.TestCase):

    def test_positive_value(self):
        """
        The functions return value when a positive integer or 0 is sent
        as the coin_quantity parameter should be the parameter value itself
        """
        self.assertEqual(process_coin_operation(2, 2), 2)

    def test_negative_value(self):
        """
        The functions return value when a negative integer is sent
        as the coin_quantity parameter should be coin_quantity value times
        two.
        """
        self.assertEqual(process_coin_operation(4, -2), -4)

    def test_negative_exception(self):
        """
        When the amount to be retrieved is more than half of what
        is currently at the drawer, an exception should be raised
        """
        self.assertRaises(Exception, process_coin_operation, 2, -4)


if __name__ == '__main__':
    unittest.main()