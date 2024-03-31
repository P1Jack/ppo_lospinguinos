import unittest
from request import get_all_dates, get_data_from_date


class TestDates(unittest.TestCase):
    def test_dates(self):
        self.assertEqual(get_all_dates(),
                          ['25-01-23', '14-02-23', '18-02-23',
                           '04-03-23', '14-03-23', '18-04-23',
                           '13-09-23', '30-09-23', '30-10-23'])

    def test_date_1(self):
        self.assertTrue(get_data_from_date('25-01-23')['correct'])

    def test_date_2(self):
        self.assertTrue(get_data_from_date('30-09-23')['correct'])

    def test_date_3(self):
        self.assertTrue(get_data_from_date('18-04-23')['correct'])

    def test_date_4(self):
        self.assertTrue(get_data_from_date('14-02-23')['correct'])

    def test_date_5(self):
        self.assertTrue(get_data_from_date('18-02-23')['correct'])

    def test_date_6(self):
        self.assertTrue(get_data_from_date('04-03-23')['correct'])


if __name__ == '__main__':
    unittest.main()
