import unittest
from vikingsClasses import Saxon
from inspect import signature


class TestSaxon(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """Setup variables and methods used by tests"""
        cls.health = 60
        cls.strength = 25
        cls.saxon = Saxon(cls.health, cls.strength)

    def testSaxonShouldReceiveTwoParams(self):
        """Test that Saxon constructor takes exactly 2 parameters"""
        self.assertEqual(len(signature(Saxon).parameters), 2)

    def testHealth(self):
        """Test that health is set correctly as instance variable"""
        self.assertEqual(self.saxon.health, self.health)

    def testStrength(self):
        """Test that strength is set correctly as instance variable"""
        self.assertEqual(self.saxon.strength, self.strength)

    def testAttack(self):
        """Test that attack is a method"""
        self.assertEqual(callable(self.saxon.attack), True)

    def testAttackShouldReceiveNoParams(self):
        """Test that attack takes no parameters"""
        self.assertEqual(len(signature(self.saxon.attack).parameters), 0)

    def testAttackREturnStrength(self):
        """Test that attack returns the strength of the saxon"""
        self.assertEqual(self.saxon.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        """Test that receiveDamage is a method"""
        self.assertEqual(callable(self.saxon.receiveDamage), True)

    def testReceiveDamageShouldReceiveOneParam(self):
        """Test that receiveDamage takes exactly 1 parameter"""
        self.assertEqual(
            len(signature(self.saxon.receiveDamage).parameters), 1)

    def testReceiveDamage(self):
        """Test that damage points are substracted from saxon's health"""
        self.saxon.receiveDamage(1)
        self.assertEqual(self.saxon.health, self.health - 1)

    def testReceiveDamageString45(self):
        """Test that receiveDamage returns a string with the result of an attack of 45 points"""
        self.assertEqual(self.saxon.receiveDamage(
            45), 'A Saxon has received 45 points of damage')

    def testReceiveDamageString10(self):
        """Test that receiveDamage returns a string with the result of an attack of 10 points"""
        self.assertEqual(self.saxon.receiveDamage(
            10), 'A Saxon has received 10 points of damage')

    def testReceiveDamageStringDied(self):
        """Test that receiveDamage returns a string notifying that the saxon has died"""
        self.assertEqual(self.saxon.receiveDamage(self.health),
                         'A Saxon has died in combat')


if __name__ == '__main__':
    unittest.main()
