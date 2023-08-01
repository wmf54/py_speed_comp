import numpy as np
import random
import time
from numba import jit
from fpi import fpi

def est_pi(n_iters):
    """
    Function to estimate pi using Monte Carlo simulation and native Python packages

    :param n_iters: number of iterations
    :type n_iters: int
    :return: and estimate of pi
    :rtype: float
    """

    # initialize the number of points in the circle and the number in the square to zero
    n_circle = 0
    n_square = 0

    # loop over the number of iterations
    for i in range(n_iters):
        # generate random value for x and y on [0.0, 1.0)
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            n_circle += 1
        n_square += 1
    pi = 4.0 * n_circle / n_square
    return pi


def vec_est_pi(n_iters):
    """
    Function to estimate pi using Monte Carlo simulation vectorized with Numpy

    :param n_iters: number of iterations
    :type n_iters: int
    :return: an estimate of pi
    :rtype: float
    """

    rng = np.random
    xy = rng.random((n_iters, 2))
    rad = xy[:, 0] ** 2 + xy[:, 1] ** 2
    n_circle = len(np.where(rad <= 1)[0])
    n_square = len(rad)
    pi = 4.0 * n_circle / n_square
    return pi


@jit(nopython=True)
def jit_est_pi(n_iters):
    """
    Function to estimate pi using Monte Carlo simulation and Numba's jit feature. Not vectorized with Numpy

    :param n_iters: number of iterations
    :type n_iters: int
    :return: an estimate of pi
    :rtype: float
    """
    n_circle = 0
    n_square = 0
    for i in range(n_iters):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            n_circle += 1
        n_square += 1
    pi = 4.0 * n_circle / n_square
    return pi


@jit(nopython=True)
def jit_vec_est_pi(n_iters):
    """
    Function to estimate pi using Monte Carlo simulation and Numba's jit feature. Vectorized with Numpy

    :param n_iters: number of iterations
    :type n_iters: int
    :return: an estimate of pi
    :rtype: float
    """
    rng = np.random
    xy = rng.random((n_iters, 2))
    r = xy[:, 0] ** 2 + xy[:, 1] ** 2
    n_circle = len(np.where(r <= 1)[0])
    n_square = len(r)
    pi = 4.0 * n_circle / n_square
    return pi


def time_func(func, iter_arr, tm_avg):
    """
    Function to time the previously defined functions over an array of iterations to make

    :param func: the Monte Carlo function to time
    :type func: function
    :param iter_arr: array-like of iteration numbers to execute
    :type iter_arr: list or np.ndarray
    :param tm_avg: a value to average the time over at each iteration
    :type tm_avg: int
    :return: an array of iteration numbers and time in msec
    :rtype: np.ndarray
    """

    # initialize the array to store time
    time_arr = np.zeros((iter_arr.shape[0], 2))

    # loop over the iteration array
    for ind, itera in enumerate(iter_arr):
        avg_time = 0  # initialize the average time variable

        # loop over the number of executions to achieve an average
        for j in range(0, tm_avg):
            # start time
            bgn_t = time.time()
            # execute the function
            func(int(itera))
            # calculate the time based on current time minus beginning
            end_t = time.time() - bgn_t
            # add this time to the average
            avg_time += end_t

        # divide by total executions
        avg_time /= tm_avg
        # convert to msec
        avg_time *= 1000
        # store the values in an array at this index
        time_arr[ind, 1] = avg_time
        time_arr[ind, 0] = int(itera)

    return time_arr


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    plt.rcParams.update({'font.size': 24})  # set the font size

    # taking one value and not averaging
    tm_avg = 1
    # generate iterations up to 10Emag
    mag = 7

    # generate the points to iterate over
    iter_arr = np.logspace(1, mag, 100)

    # set some lists of stuff like labels for plotting, the functions, and colors for plotting
    labels = ['Python', 'Vectorized Python', 'Numba Python', 'Vectorized Numba Python', 'Fortran', 'Vectorized Fortran']
    funcs = [est_pi, vec_est_pi, jit_est_pi, jit_vec_est_pi, fpi.dofpi, fpi.vfpi]
    colors = ['darkgreen', 'limegreen', 'darkblue', 'cyan', 'darkred', 'magenta']

    # initialize the plot objects
    fig, ax = plt.subplots()
    # loop over and time each function
    for func, lbl, color in zip(funcs, labels, colors):
        # time the function
        time_arr = time_func(func, iter_arr, tm_avg)
        # plot the results
        ax.plot(time_arr[:, 0], time_arr[:, 1], marker='x', color=color, label=lbl)

    # Just the fast ones a little further
    # New iteration array that extends from 10Emag to 10E(mag+2)
    iter_arr = np.logspace(mag, mag + 1, 100)

    # set some lists of stuff like labels for plotting, the functions, and colors for plotting
    labels = ['Vectorized Python', 'Numba Python', 'Vectorized Numba Python', 'Fortran', 'Vectorized Fortran']
    funcs = [vec_est_pi, jit_est_pi, jit_vec_est_pi, fpi.dofpi, fpi.vfpi]
    colors = ['limegreen', 'darkblue', 'cyan', 'darkred', 'magenta']

    # loop over and time each function
    for func, lbl, color in zip(funcs, labels, colors):
        # time the function
        time_arr = time_func(func, iter_arr, tm_avg)
        # plot the results
        ax.plot(time_arr[:, 0], time_arr[:, 1], marker='x', color=color)

    # set plot scales, lebels, etc.
    ax.set_xscale('log')
    ax.set_xlabel('Number of Iterations')
    ax.set_ylabel('Average Time to Execute, msec')
    ax.legend()
    plt.show()
