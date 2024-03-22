import unittest
from Sample import slicing,formatting,concatenation,manipulation
class Test_strings(unittest.TestCase):
    def test_slicing(self):
        self.assertEqual(slicing('sruthi'),"uthi")
        self.assertEqual(slicing("Krishna"),'ishna')
    def test_formatting(self):
        self.assertEqual(formatting('Harshini'),'Hello welcome to Harshini')
        self.assertEqual(formatting('Harshini'),'Hello welcome to Harshini')
    def test_concatenation(self):
        self.assertEqual(concatenation('Sree Latha'),'Happy Coding Sree Latha')
        self.assertEqual(concatenation('Madhurima'),'Happy Coding Madhurima')
    def test_manipulation(self):
        self.assertEqual(manipulation('suman'),'SUMAN,suman,suman,sumhn')
        self.assertEqual(manipulation(' latha'),' LATHA, latha,latha, lhthh')
if __name__=="__main__":
    unittest.main()