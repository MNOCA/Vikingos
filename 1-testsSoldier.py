import unittest
from vikingsClasses import Soldier
from inspect import signature


class TestSoldier(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """Setup variables and methods used by tests"""
        cls.strength = 150
        cls.health = 300
        cls.soldier = Soldier(cls.health, cls.strength)

    def testConstructorSignature(self):
        """Test that Soldier constructor takes exactly 2 parameters"""
        self.assertEqual(len(signature(Soldier).parameters), 2)

    def testHealth(self):
        """Test that health is set correctly as instance variable"""
        self.assertEqual(self.soldier.health, self.health)

    def testStrength(self):
        """Test that strength is set correctly as instance variable"""
        self.assertEqual(self.soldier.strength, self.strength)

    def testAttackShouldBeFunction(self):
        """Test that attack is a method"""
        self.assertEqual(callable(self.soldier.attack), True)

    def testAttackHasNoParams(self):
        """Test that attack takes no parameters"""
        self.assertEqual(len(signature(self.soldier.attack).parameters), 0)

    def testAttackRetunsStrength(self):
        """Test that attack returns the strength of the soldier"""
        self.assertEqual(self.soldier.attack(), self.strength)

    def testReceivesDamage(self):
        """Test that receiveDamage is a method"""
        self.assertEqual(callable(self.soldier.receiveDamage), True)

    def testReceivesDamageHasParams(self):
        """Test that receiveDamage takes exactly 1 parameter"""
        self.assertEqual(
            len(signature(self.soldier.receiveDamage).parameters), 1)

    def testReceiveDamageReturnNone(self):
        """Test that receiveDamage returns None"""
        self.assertEqual(self.soldier.receiveDamage(50), None)

    def testCanReceiveDamage(self):
        """Test that damage points are substracted from soldier's health"""
        self.soldier.receiveDamage(50)
        self.assertEqual(self.soldier.health, self.health - 50)


if __name__ == '__main__':
    unittest.main()
