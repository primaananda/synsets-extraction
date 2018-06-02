import unittest
import json

from synsets import synsets_gen
 

class SyncSetTest(unittest.TestCase):
    
    # def test_sample(self):
    #     input = synsets_gen('ahad', open('datatest/1.json'))
    #     output = [['ahad', 'minggu'], ['ahad', 'esa', 'satu', 'tunggal']]
    #     self.assertEqual(input, output, 'first test case pass')
    #
    # def test_sample2(self):
    #     input = synsets_gen('setanggi', open('datatest/2.json'))
    #     output = [[]]
    #     self.assertEqual(input, output, '2nd test case pass')
    #
    # def test_sample3(self):
    #     input = synsets_gen('aborsi', open('datatest/3.json'))
    #     output = [['aborsi', 'pengguguran']]
    #     self.assertEqual(input, output, '3rd test case pass')
    #
    # def test_sample4(self):
    #     input = synsets_gen('pekan', open('datatest/4.json'))
    #     output = [['pasar','pekan', 'rekan'], ['minggu', 'pekan']]
    #     self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))
    
    def test_sample5(self):
        input = synsets_gen('perdamaian', open('datatest/5.json'))
        output = [['peleraian','perbaikan', 'perdamaian']]
        self.assertEqual(input, output, '\nresult: {}\nexpected: {}'.format(input, output))
    
if __name__ == '__main__':
    unittest.main()
