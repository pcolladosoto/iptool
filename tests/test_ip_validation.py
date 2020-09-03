import unittest, argparse
from iptool import arg_parsing

# Note that having a test case reach its end is having it passed

class test_ip_validation(unittest.TestCase):
    def test_neg_octect(self):
        init = "10.-1.10.0"
        try:
            arg_parsing.check_valid_ip(init, argparse.ArgumentParser())
        except SystemExit:
            pass
        else:
            self.fail("Didn't exit!")

    def test_big_octect(self):
        init = "10.3.256.0"
        try:
            arg_parsing.check_valid_ip(init, argparse.ArgumentParser())
        except SystemExit:
            pass
        else:
            self.fail("Didn't exit!")

    def test_not_int(self):
        init = "10.a.10.0"
        try:
            arg_parsing.check_valid_ip(init, argparse.ArgumentParser())
        except SystemExit:
            pass
        else:
            self.fail("Didn't exit!")

if __name__ == '__main__':
    unittest.main()