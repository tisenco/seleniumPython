from common import open_baidu
from read_ini import bddw
driver=open_baidu("https://www.baidu.com")
import unittest
class baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start-test")
    @classmethod
    def tearDownClass(cls):
        print("end_test")
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test01(self):
        driver.find_element_by_id(bddw()[1]).send_keys("周润发")
        print("构建成功")
if __name__=="__main__":
    unittest.main()
