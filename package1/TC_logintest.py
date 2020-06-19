import unittest
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    def test_loginemail(self):
        print("this is login my email")
        self.assertTrue(True)

    def test_loginFacebook(self):
        print("this is login my facebook")
        self.assertTrue(True)

    def test_loginTwitter(self):
        print("this is login my Twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/mchan/PycharmProjects/seleniumtesting/reports"))
