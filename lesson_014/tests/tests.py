# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase

from bowling import check_errors, get_score
from woldwide import get_score_woldwide


class Test(TestCase):

    def test_get_score_value(self):
        with self.assertRaisesRegex(ValueError, 'Введено неправильное значение - 0'):
            check_errors('X340/1744XX23--4/')

    def test_strike_second_throw(self):
        with self.assertRaisesRegex(ValueError, 'Strike на втором броске'):
            check_errors('1X422/1744XX23--4/')

    def test_spare_first_throw(self):
        with self.assertRaisesRegex(ValueError, 'Spare на первом броске'):
            check_errors('/34-/1744XX23--4/')

    def test_no_second_throw_after_strike(self):
        with self.assertRaisesRegex(Exception, 'Введено неправильное значение после strike'):
            get_score('3532X333/2/62--62X1')

    def test_incorrect_frames(self):
        with self.assertRaisesRegex(Exception, 'Не правильное количество фреймов!'):
            get_score('1744XX23--4/')

    def test_all_strikes(self):
        self.score = get_score(result='XXXXXXXXXX')
        self.assertEqual(200, self.score)

    def test_simple_frame_woldwide(self):
        self.score = get_score_woldwide(result='526-2223434/2/X351/')
        self.assertEqual(97, self.score)

    def test_all_strikes_woldwide(self):
        self.score = get_score_woldwide(result='XXXXXXXXXX')
        self.assertEqual(270, self.score)


if __name__ == '__main__':
    unittest.main()
