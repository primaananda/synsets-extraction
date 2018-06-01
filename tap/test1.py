import unittest

from main import synsets_gen
 

class SyncSetTest(unittest.TestCase):
    
    def test_sample(self):
        input = synsets_gen('ahad')
        output = [['ahad', 'minggu'], ['ahad', 'esa', 'satu', 'tunggal']]
        self.assertEqual(input, output, 'first test case pass')
    
    def test_sample2(self):
        input = synsets_gen('setanggi')
        output = [[]]
        self.assertEqual(input, output, '2nd test case pass')
    
    def test_sample3(self):
        input = synsets_gen('aborsi')
        output = [['aborsi', 'pengguguran']]
        self.assertEqual(input, output, '3rd test case pass')
    
    def test_sample4(self):
        input = synsets_gen('minggu')
        output = [['ahad','minggu', 'pekan']]
        self.assertEqual(input, output, '4rd test case pass')

if __name__ == '__main__':
    unittest.main()
