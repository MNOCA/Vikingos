import unittest
from vikingsClasses import Viking, Saxon, War
import random

class TestWarRoutine(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.viking_names = ['Erik', 'Leif', 'Bjorn', 'Ragnar', 'Ivar', 'Olaf', 'Sigurd', 'Harald', 'Ulf', 'Gunnar']
        cls.war = War()

        for name in cls.viking_names:
            viking = Viking(name, 100, random.randint(90, 100))
            cls.war.addViking(viking)

        for _ in range(10):
            saxon = Saxon(100, random.randint(90, 100))
            cls.war.addSaxon(saxon)

    # Check if the Viking army has exactly 10 Vikings
    def test_initial_army_counts(self):
        self.assertEqual(len(self.war.vikingArmy), 10)

    # Check if the Saxon army has exactly 10 Saxons
    def test_saxon_army_counts(self):
        self.assertEqual(len(self.war.saxonArmy), 10)

    # Check if Vikings won
    def test_vikings_win(self):
        self.war.saxonArmy = []
        winner = self.war.showStatus()
        self.assertEqual(winner, 'Vikings have won the war of the century!')

    # Check if Saxons won
    def test_saxons_win(self):
        self.war.vikingArmy = []
        winner = self.war.showStatus()
        self.assertEqual(winner, 'Saxons have fought for their lives and survive another day...')

    # Check if battle is still ongoing
    def test_battle_status(self):
        status = self.war.showStatus()
        self.assertEqual(status, 'Vikings and Saxons are still in the thick of battle.')

if __name__ == '__main__':
    unittest.main()
