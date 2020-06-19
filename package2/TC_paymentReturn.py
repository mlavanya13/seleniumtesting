import unittest
import HtmlTestRunner

class paymentReturn(unittest.TestCase):
    def test_paymentReturn(self):
        print("this is payment Return Test")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/mchan/PycharmProjects/seleniumtesting/reports"))