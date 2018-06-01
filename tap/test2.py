import unittest

from main import sync_set_gen


class SyncSetTest(unittest.TestCase):
    
    def test_sample(self):
        input = sync_set_gen('setanggi')
        output = []
        self.assertEqual(input, output, 'first test case pass')

if __name__ == '__main__':
    unittest.main()
