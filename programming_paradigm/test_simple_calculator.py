import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        #invalid inputs should raise ValueError
        self.assertRaises(ValueError,self.calc.add, 'r',5)
        self.assertRaises(ValueError,self.calc.add, 5,'r')
        #missing arguments rises TypeError
        self.assertRaises(TypeError,self.calc.add, 5)
        
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        '''test subraction method'''
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        #invalid inputs should raise ValueError
        self.assertRaises(ValueError,self.calc.subtract, 'r',5)
        self.assertRaises(ValueError,self.calc.subtract, 5,'r')
        #missing arguments rises TypeError
        self.assertRaises(TypeError,self.calc.subtract, 5)
    
    def test_multiplication(self):
        '''test multiplication method'''
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        #invalid inputs should raise ValueError
        self.assertRaises(ValueError,self.calc.multiply, 'r',5)
        self.assertRaises(ValueError,self.calc.multiply, 5,'r')
        #missing arguments rises TypeError
        self.assertRaises(TypeError,self.calc.multiply, 5)

    def test_division(self):
        '''test division'''
        self .assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        #invalid inputs should raise ValueError
        self.assertRaises(TypeError,self.calc.divide, 'r',5)
        self.assertRaises(TypeError,self.calc.divide, 5,'r')
        #test zero division
        self.assertRaises(ZeroDivisionError,self.calc.divide, 1,0)

# Remember to write additional test methods for subtract, multiply, and divide.