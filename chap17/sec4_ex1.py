import scipy
import numpy as np


def gaussian(x: float, mu: float, sigma: float) -> float:
    return np.e ** -(((x - mu) ** 2) / (2 * sigma**2)) / (
        sigma * ((2 * np.pi) ** 0.5)
    )


print(scipy.integrate.quad(gaussian, -1, 1, (0, 1))[0])
