
import numpy as np
from ms_thermo.tadia import tadia_table


def test_tadia_table():
	
	burned_t, yburnt = tadia_table(300,101325,1)
	target_value = 2312.990462472097

	np.testing.assert_allclose(target_value, burned_t, rtol=10e-6)

	target_value = [0.7180953905274218, 0, -3.206589963833384e-07, 0.20002461953348916, 0.0818803105980856]
	np.testing.assert_allclose(target_value, [k for k in yburnt.values()], rtol=10e-6)
