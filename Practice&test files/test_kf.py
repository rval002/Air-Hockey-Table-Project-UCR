import numpy as np
from kf import KF
import unittest


class TestKF(unittest.TestCase):
        def test_can_construct_with_xand_v(self):
            x = 0.2
            v = 2.3

            kf = KF(initx = x, initv = v)
            self.assertAlmostEqual(kf.x[0],x)
            self.assertAlmostEqual(kf.x[1],v)
