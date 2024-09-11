import unittest
from vikingsClasses import War, Viking, Saxon
from inspect import signature


class TestWar(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.war = War()

    def testWarShouldReciveNoParams(self):
        """Test that war instance takes no parameter"""
        self.assertEqual(len(signature(War).parameters), 0)

    def testVikingArmy(self):
        """Test that viking army is empty at first"""
        self.assertEqual(self.war.vikingArmy, [])

    def testSaxonArmy(self):
        """Test that saxon army is empty at first"""
        self.assertEqual(self.war.saxonArmy, [])


class TestWar2(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """setup variables and methods used by tests"""
        def generateViking():
            cls.name = 'Harald'
            cls.strength = 150
            cls.health = 300
            return Viking(cls.name, cls.health, cls.strength)

        def generateSaxon():
            cls.health = 60
            cls.strength = 25
            return Saxon(cls.health, cls.strength)

        cls.viking = generateViking()
        cls.saxon = generateSaxon()
        cls.war = War()
        cls.war.addSaxon(cls.saxon)
        cls.war.addViking(cls.viking)

    def testAddViking(self):
        """Test if addViking method is callable"""
        self.assertEqual(callable(self.war.addViking), True)

    def testAddVikingShouldReceiveOneParam(self):
        """Test if addViking takes exactly 2 parameters"""
        self.assertEqual(len(signature(self.war.addViking).parameters), 1)

    def testAddVikingInList(self):
        """Test if addViking added viking passed as argument to vikingArmy list"""
        self.assertEqual(self.war.vikingArmy, [self.viking])

    def testAddVikingReturnNull(self):
        """Test if addViking method returns None"""
        self.assertEqual(self.war.addViking(self.viking), None)

    def testAddSaxonShouldBeFunction(self):
        """Test if addSaxon method is callable"""
        self.assertEqual(callable(self.war.addSaxon), True)

    def testAddSaxonReceiveOneParam(self):
        """Test if addSaxon takes exactly one parameter"""
        self.assertEqual(len(signature(self.war.addSaxon).parameters), 1)

    def testSaxonArmyReturnEmptyList(self):
        """Test if addSaxon added saxon passed as argument to saxonArmy list"""
        self.assertEqual(self.war.saxonArmy, [self.saxon])

    def testAddSaxonReturnNone(self):
        """Test if addSaxon method returns None"""
        self.assertEqual(self.war.addSaxon(self.saxon), None)

    def testVikingAttackIsFunction(self):
        """Test if vikingAttack method is callable"""
        self.assertEqual(callable(self.war.vikingAttack), True)

    def testVikingAttackReceiveNoParam(self):
        """Test if vikingAttack method takes no parameter"""
        self.assertEqual(len(signature(self.war.vikingAttack).parameters), 0)

    def testSaxonHealth(self):
        """Test if saxon health decreased by viking strength during an attack"""
        oldHealt = self.saxon.health
        self.war.vikingAttack()
        self.assertEqual(self.saxon.health, oldHealt - self.viking.strength)

    def testVikingAttack(self):
        """Test that vikingAttack removed dead saxon from saxonArmy"""
        self.war.vikingAttack()
        self.assertEqual(len(self.war.saxonArmy), 0)

    def testAddSaxon(self):
        """Test that viking attacks returns the correct string (saxon is dead)"""
        print(self.war.__dict__)
        self.assertEqual(self.war.vikingAttack(), 'A Saxon has died in combat')

    def testSaxonAttackIsFunction(self):
        """Test that saxonAttack is callable"""
        self.assertEqual(callable(self.war.saxonAttack), True)

    def testSaxonAttackReceiveNoParam(self):
        """Test that saxonAttack takes no parameter"""
        self.assertEqual(len(signature(self.war.saxonAttack).parameters), 0)

    def testVikingHealth(self):
        """Test if viking health decreased by saxon strength during an attack"""
        oldHealt = self.viking.health
        self.war.saxonAttack()
        self.assertEqual(self.viking.health, oldHealt - self.saxon.strength)

    def testVikingArmyList(self):
        """Test that saxonAttack removed dead viking from vikingArmy"""
        for i in range(12):
            if(len(self.war.vikingArmy) == 0):
                break
            self.war.saxonAttack()
        self.assertEqual(len(self.war.vikingArmy), 0)

    def testReturnOfSaxonAttack(self):
        """Test that saxonAttack returns a string with the effect of the attack on viking"""
        self.assertEqual(self.war.saxonAttack(), self.viking.name +
                         ' has received ' + str(self.saxon.strength) + ' points of damage')

    def testShowStatusShouldIsFunction(self):
        """Test that showStatus is callable"""
        self.assertEqual(callable(self.war.showStatus), True)

    def testShowStatusReceiveNoParams(self):
        """Test that showStatus takes no parameter"""
        self.assertEqual(len(signature(self.war.showStatus).parameters), 0)

    def testShouldReturnStringVikingsWon(self):
        """Test that showStatus returns the correct string when vikings have won"""
        self.war.vikingAttack()
        self.assertEqual(self.war.showStatus(),
                         'Vikings have won the war of the century!')

    def testShouldReturnStringSaxonsWon(self):
        """Test that showStatus returns the correct string when saxons have won"""
        for i in range(12):
            self.war.saxonAttack()
        self.assertEqual(self.war.showStatus(
        ), 'Saxons have fought for their lives and survive another day...')

    def testShouldReturnStringStillFighting(self):
        """Test that showStatus returns the correct string when war is no over yet"""
        self.assertEqual(
            self.war.showStatus(), 'Vikings and Saxons are still in the thick of battle.')


if __name__ == '__main__':
    unittest.main()
