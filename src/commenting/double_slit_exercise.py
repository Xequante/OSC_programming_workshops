"""
This code generates an image of a double slit aperture.

Your task is to go through each line and write a comment explaining what is
being done at each step.  If you are struggling to identify the purpose of a
given line, try to use breakpoints to investigate what is going on

To run this code, type in main.py
>>> from src.commenting.double_slit_exercise import *
where the * is a wild card import.  Then, add under main():
>>> plot_double_slit_aperture()
"""


import numpy as np
from matplotlib import pyplot as plt


def plot_double_slit_aperture(w: float = 5, h: float = 100, d: float = 40):
    """
    <Description of the code>

    :param w:
    :param h:
    :param d:
    """
    aperture, x_coords, y_coords = double_slit_aperture(w=w, h=h, d=d)
    fig, ax = plt.subplots(1)
    dx = (x_coords[1] - x_coords[0]) / 2.
    dy = (y_coords[1] - y_coords[0]) / 2.
    extent = [x_coords[0] - dx, x_coords[-1] + dx,
              y_coords[0] - dy, y_coords[-1] + dy]
    ax.imshow(aperture, extent=extent, cmap='gray')
    plt.show()


def double_slit_aperture(w: float = 5, h: float = 100, d: float = 40,
                         n: int = 1001, square=True):
    """
    <Description of the code>

    :param w:
    :param h:
    :param d:
    :param n:
    :param square:
    :return:
    """

    if w > d:
        raise SyntaxError('The distance between slits should be larger than '
                          'their width')
    x_req: int = int(w + d)
    y_req: int = int(h)
    if square:
        x_req = max(x_req, y_req)
        y_req = x_req
    x_coords = np.linspace(-x_req, x_req, n)
    y_coords = np.linspace(-y_req, y_req, n)
    aperture = np.zeros((n, n))
    X, Y = np.meshgrid(x_coords, y_coords)
    x_trans = np.logical_and((np.abs(X) < (d + w) / 2),
                             (np.abs(X) > (d - w) / 2))
    y_trans = (np.abs(Y) < h / 2)
    aperture[np.logical_and(x_trans, y_trans)] = 1
    return aperture, x_coords, y_coords

