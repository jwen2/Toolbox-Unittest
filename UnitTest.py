import unittest
import Functions

class TestRemoveNegs(unittest.TestCase):


    def test_removesneg(self):
        self.assertEqual(Functions.remove_neg([25,-15,1,2,3,-4]), [25,1,2,3])
        self.assertEqual(Functions.remove_neg([-1,-2,-3,-4,-5]), [])
        self.assertEqual(Functions.remove_neg([99,98,97,-96,96,95,-94]), [99,98,97,96,95])
        self.assertEqual(Functions.remove_neg([-1,0,1]), [0,1])

    def test_longername(self):
        self.assertEqual(Functions.longername('Mary','Jane'), 'They are they same length')
        self.assertEqual(Functions.longername('Maryyy','Jane'), 'Maryyy')
        self.assertEqual(Functions.longername('Mary','Janeee'), 'Janeee')


if __name__ == '__main__':
    unittest.main()
