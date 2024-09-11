import unittest
from vikingsClasses import Viking
from inspect import signature


class TestViking(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """Setup variables and methods used by tests"""

        cls.name = 'Harald'
        cls.strength = 150
        cls.health = 300
        cls.viking = Viking(cls.name, cls.health, cls.strength)

    def testShouldReciveThreeParams(self):
        """Test that Viking constructor takes exactly 3 parameters"""
        self.assertEqual(len(signature(Viking).parameters), 3)

    def testName(self):
        """Test that name is set correctly as instance variable"""
        self.assertEqual(self.viking.name, self.name)

    def testHealth(self):
        """Test that health is set correctly as instance variable"""
        self.assertEqual(self.viking.health, self.health)

    def testStrenght(self):
        """Test that strength is set correctly as instance variable"""
        self.assertEqual(self.viking.strength, self.strength)

    def testAttackShouldBeFunction(self):
        """Test that attack is a method"""
        self.assertEqual(callable(self.viking.attack), True)

    def testAttackReciveNoParameters(self):
        """Test that attack takes no parameters"""
        self.assertEqual(len(signature(self.viking.attack).parameters), 0)

    def testAttackShouldReturnStrength(self):
        """Test that attack returns the strength of the viking"""
        self.assertEqual(self.viking.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        """Test that receiveDamage is a method"""
        self.assertEqual(callable(self.viking.receiveDamage), True)

    def testReceiveDamageReciveOneParam(self):
        """Test that receiveDamage takes exactly 1 parameter"""
        self.assertEqual(
            len(signature(self.viking.receiveDamage).parameters), 1)

    def testReciveDamageShouldRestHealth(self):
        """Test that damage points are substracted from viking's health"""
        self.viking.receiveDamage(50)
        self.assertEqual(self.viking.health, self.health - 50)

    def testReciveDamageShouldReturnString50(self):
        """Test that receiveDamage returns a string with the result of am attack of 50 points"""
        self.assertEqual(self.viking.receiveDamage(50), self.name +
                         ' has received 50 points of damage')

    def testReciveDamageShouldReturnString70(self):
        """Test that receiveDamage returns a string with the result of an attack of 70 points"""
        self.assertEqual(self.viking.receiveDamage(70), self.name +
                         ' has received 70 points of damage')

    def testReceiveDamageShouldReturnStringDeath(self):
        """Test that receiveDamage returns a string notifying that the viking is dead"""
        self.assertEqual(self.viking.receiveDamage(self.health),
                         self.name + ' has died in act of combat')

    def testBattleCry(self):
        """Test that battleCry is a method"""
        self.assertEqual(callable(self.viking.battleCry), True)

    def testBattleCryReturnString(self):
        """Test that battleCry returns the correct battleCry string"""
        self.assertEqual(self.viking.battleCry(), 'Odin Owns You All!')


if __name__ == '__main__':
    unittest.main()
