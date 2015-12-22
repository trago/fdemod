from __future__ import division
import numpy as np
cimport numpy as np

cpdef gaussian1D(double sigma):
    """
    Generates a one-dimensional gaussian kernel with parameter sigma.
    
    The size of this kernel is determined by sigma. This kernel is generated
    using the equation of the normal distribution.
    
    :param sigma: The width of the gaussian
    :type sigma: Real double
    :returns: numpy array, type double
    """
    pass
    
cpdef gabor1D(double sigma, double w0):
    """
    Generates a one-dimensional gabor kernel with parameter sigma.
    
    It uses the function :func:`guassuan1D` to generate a gabor filter.
    
    :param sigma: The width of the gabor filter
    :param type: Real double
    :param w0: The frequency where this kernel is tune
    :returns: numpy array, type complex double
    """
    pass