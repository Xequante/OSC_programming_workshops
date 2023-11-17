"""
This is a commented version of the code which generates an image of a
double slit aperture.  All the code is exactly the same, the only difference
between the files is the commenting
"""


import numpy as np
from matplotlib import pyplot as plt


def plot_double_slit_aperture(w: float = 5, h: float = 100, d: float = 40):
    """
    Plots a double slit aperture

    :param w: width of each slit
    :param h: height of each slit
    :param d: distance between the slits
    """

    # Obtain the aperture from the "double_slit_aperture()" function
    aperture, x_coords, y_coords = double_slit_aperture(w=w, h=h, d=d)

    # Create a figure and an axis to plot on
    fig, ax = plt.subplots(1)

    # Identify the extent of the image being depicted
    dx = (x_coords[1] - x_coords[0]) / 2.
    dy = (y_coords[1] - y_coords[0]) / 2.
    extent = [x_coords[0] - dx, x_coords[-1] + dx,
              y_coords[0] - dy, y_coords[-1] + dy]

    # Plot the aperture on the axis using imshow with a gray colormap
    ax.imshow(aperture, extent=extent, cmap='gray')

    # Display the plot
    plt.show()


def double_slit_aperture(w: float = 5, h: float = 100, d: float = 40,
                         n: int = 1001, square=True):
    """
    Generates an array for a double slit aperture, where each element of the
    array ranges from 0 (where no light passes through the aperture) to 1
    (where all of the light passes through the aperture).

    Presently, this is a basic version which sets a coordinate to have a
    transmission of 100% if the coordinate is within the aperture, and 0% if
    the coordinate is outside of the aperture.

    :param w: width of each slit
    :param h: height of each slit
    :param d: distance between the slits
    :param n: resoulution of the image (will be shifted to nearest odd number)
    :param square: Specify if you want the aperture to be square
    :return: array of light passing through each discritized coordinate
    """

    # Make sure the distance between the slits is longer than their width
    if w > d:
        raise SyntaxError('The distance between slits should be larger than '
                          'their width')

    # Compute the number of pixels we need in the x and y directions
    x_req: int = int(w + d)
    y_req: int = int(h)

    # Set x_req = y_req = max(x_req, y_req) if we want a square output
    if square:
        x_req = max(x_req, y_req)
        y_req = x_req

    # Get the x and y coordinates
    x_coords = np.linspace(-x_req, x_req, n)
    y_coords = np.linspace(-y_req, y_req, n)

    # Create the array where we will record the transmission of the aperture
    aperture = np.zeros((n, n))

    # Obtain a meshgrid of the X and Y coordinates of each pixel
    X, Y = np.meshgrid(x_coords, y_coords)

    # Identify array elements with 100% transmission in the X direction
    x_trans = np.logical_and((np.abs(X) < (d + w) / 2),
                             (np.abs(X) > (d - w) / 2))

    # Identify array elements with 100% transmission in the Y direction
    y_trans = (np.abs(Y) < h / 2)

    # Set the aperture value of these pixels to 1
    aperture[np.logical_and(x_trans, y_trans)] = 1

    # Return the aperture and the relevant coordinates
    return aperture, x_coords, y_coords
