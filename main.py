import spectrochempy as scp

from spectrochempy import NDDataset
from spectrochempy import Coord
from scipy.integrate import simpson
import matplotlib as plt
from numpy import trapz


script = """

#-----------------------------------------------------------
# syntax for parameters definition :
# name : value, low_bound,  high_bound
#  * for fixed parameters
#  $ for variable parameters
#  > for reference to a parameter in the COMMON block
#    (> is forbidden in the COMMON block)
# common block parameters should not have a _ in their names
#-----------------------------------------------------------
#

MODEL: Gauss_1
shape: gaussianmodel
$ ampl: 3, 0.0, None
* width: 8, 0.0, None
* pos: 21.6, 0,  69

MODEL: Gauss_2
shape: gaussianmodel
$ ampl: 4, 0.0, None
* width: 12, 0.0, None
* pos: 33.6, 0,  69

"""

data = NDDataset(
    [52.92794155,
        53.01758847,
        52.68084518,
        52.56689951,
        51.97182424,
        52.0888804,
        52.51319987,
        52.23700272,
        52.1039677,
        52.2132027,
        52.91907902,
        53.08059311,
        53.27510601,
        53.67633211,
        53.83257563,
        53.8949178,
        54.27121638,
        54.66266351,
        55.16475595,
        55.40401714,
        55.25327843,
        55.42933108,
        54.79692604,
        54.72990824,
        54.53681964,
        54.77241537,
        54.46132026,
        53.6943212,
        52.8145051,
        52.27392625,
        52.41466482,
        51.71078385,
        51.03631581,
        50.36213192,
        49.97073309,
        49.51736895,
        49.32948463,
        48.76992745,
        48.02633964,
        48.13414312,
        48.16069304,
        47.27334489,
        47.28018978,
        46.87284001,
        46.72019651,
        46.08872907,
        45.79069298,
        45.13185988,
        45.29172406,
        45.14499292,
        44.4114587,
        44.68572943,
        44.52103858,
        44.25293836,
        44.08093927,
        44.04577797,
        44.02180298,
        43.87744839,
        43.7863766,
        44.11891469,
        44.15185251,
        44.00001516,
        43.89619196,
        43.64927786,
        43.258989,
        42.8795812,
        42.95684263,
        42.81112905],
    name="Dataset N1", 
    author="Blake and Mortimer", 
    description="A dataset from scratch",
    dims=['y'],
)

# Define a Gaussian model
gaussian_model = Gaussian()

# Fit the model to the data
fit_result = data.fit(gaussian_model)

# Extract the parameters from the fit result
amplitude = fit_result['ampl'].value
width = fit_result['width'].value
position = fit_result['pos'].value

# Print the results
print(f"The amplitude of the Gaussian peak is: {amplitude}")
print(f"The width of the Gaussian peak is: {width}")
print(f"The position (centroid) of the Gaussian peak is: {position}")
