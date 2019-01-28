#_author='bei'
#-*- coding=utf-8 -*-

import unittest
import requests

class Testlogin(unittest.TestCase):

    def setUp(self):
        print("test login start:")
        self.url = "http://127.0.0.1:8000/login"
    def tearDown(self):
        print("test login done!")

    def test_login_01(self):
        print("test login case_01  doing...")

        data={"username":"yang","password":"1234"}
        result = requests.post(self.url.data)
        #print result.status_code
        assert result.status_code==200,"test login failed!"

    def test_login_02(self):
        print("test login case_02 doing...")

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testlogin("test_login_02"))
    suit.addTest(Testlogin("test_login_01"))

    runner = unittest.TextTestRunner()
    runner.run(suit)