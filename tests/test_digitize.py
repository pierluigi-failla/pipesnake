# -*- coding: utf-8 -*-

import unittest

from pipesnake.transformers.stats import Digitize


class TestDigitize(unittest.TestCase):
    def test_digitize(self):
        from _data import x
        from _data import y

        digitizer = Digitize(x_cols='all', y_cols='all')
        x_new, y_new = digitizer.fit_transform(x, y)
        self.assertTrue(x_new.min().all() == 0, 'min is not 0')
        self.assertTrue(y_new.min().all() == 0, 'min is not 0')
        self.assertTrue(x_new.max().all() == 1, 'min is not 1')
        self.assertTrue(y_new.max().all() == 1, 'min is not 1')

        del x, y, x_new, y_new