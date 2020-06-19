import unittest
import HtmlTestRunner


class paymenttest(unittest.TestCase):
    def test_paymenttest(self):
        print("this is payment Test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/mchan/PycharmProjects/seleniumtesting/reports"))
