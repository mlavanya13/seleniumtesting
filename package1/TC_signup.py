import unittest
import HtmlTestRunner

class SignupTest(unittest.TestCase):
    def test_signupemail(self):
        print("this is signup my email")
        self.assertTrue(True)
    def test_signupFacebook(self):
        print("this is signup my facebook")
        self.assertTrue(True)
    def test_signupTwitter(self):
        print("this is signup my Twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/mchan/PycharmProjects/seleniumtesting/reports"))