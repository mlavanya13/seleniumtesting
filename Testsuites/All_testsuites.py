import unittest
from package1.TC_logintest import LoginTest
from package1.TC_signup import SignupTest

from package2.TC_paymentReturn import paymentReturn
from package2.TC_paymenttest import paymenttest

#Get all the tests

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymentReturn)
tc4=unittest.TestLoader().loadTestsFromTestCase(paymenttest)

#create test suite
#unittest.TestSuite()
#sanityTestsuite = unittest.TestSuite([tc1,tc2])
#unittest.TextTestRunner().run(sanityTestsuite)
#functionalTestsuite = unittest.TestSuite([tc3,tc4])
#unittest.TextTestRunner().run(functionalTestsuite)
masterTestsuite = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(masterTestsuite)


