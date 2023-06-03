import unittest
from calculadora_nba import NBAStatsCalculator

class TestNBAStatsCalculator(unittest.TestCase):
    def setUp(self):
        self.calculadora = NBAStatsCalculator()

    def test_calcular_fg_percent(self):
        self.calculadora.field_goal_made = 6
        self.calculadora.field_goal_attempted = 14
        self.assertEqual(self.calculadora.calcular_fg_percent(), 0.42857142857142855)

    def test_calcular_3pt_percent(self):
        self.calculadora.three_point_shot_made = 1
        self.calculadora.three_point_shot_attempted = 2
        self.assertEqual(self.calculadora.calcular_3pt_percent(), 0.5)

    def test_calcular_ftr(self):
        self.calculadora.freethrow_made = 8
        self.calculadora.freethrow_attempted = 10
        self.assertEqual(self.calculadora.calcular_ftr(), 0.8)

    def test_calcular_assists_per_turnover(self):
        self.calculadora.assists = 8
        self.calculadora.turnovers = 2
        self.assertEqual(self.calculadora.calcular_assists_per_turnover(), 4.0)

    def test_calcular_2pt_percent(self):
        self.calculadora.field_goal_attempted = 12
        self.calculadora.field_goal_made = 6
        self.assertEqual(self.calculadora.calcular_2pt_percent(), 0.5)

    def test_calcular_ts_percent(self):
        self.calculadora.points = 20
        self.calculadora.field_goal_attempted = 12
        self.assertEqual(self.calculadora.calcular_ts_percent(), 0.8333333333333334)

if __name__ == '__main__':
    unittest.main()