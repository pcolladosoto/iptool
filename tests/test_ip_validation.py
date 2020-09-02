import unittest, argparse
from iptool import arg_parsing

class test_ip_validation(unittest.TestCase):
    def test_neg_octect(self):
        init = "10.-1.10.0"
        self.assertRaises(argparse.ArgumentTypeError, arg_parsing.check_valid_ip, init)

    def test_big_octect(self):
        init = "10.3.256.0"
        self.assertRaises(argparse.ArgumentTypeError, arg_parsing.check_valid_ip, init)

    def test_not_int(self):
        init = "10.a.10.0"
        self.assertRaises(argparse.ArgumentTypeError, arg_parsing.check_valid_ip, init)

if __name__ == '__main__':
    unittest.main()