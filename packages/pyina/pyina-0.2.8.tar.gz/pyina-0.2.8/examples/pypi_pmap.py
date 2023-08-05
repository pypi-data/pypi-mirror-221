#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2023 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/pyina/blob/master/LICENSE

__doc__ = """
# The standard MPI example, computes the integral 
# 
# Integrate[4/(1+x^2),{x,0,1}]
# 
# numerically, and in parallel.
# To run:

alias mpython='mpiexec -np [#nodes] `which python`'
mpython pypi_pmap.py

# A few warnings:
#  - Evaluating this integral is a horrible way to get the value of Pi
#  - Uniform sampling (or the trapezoidal rule, as implemented here) is
#    a horrible way to get the value of the integral
#
# For speed, use scipy instead, which provides the bindings to quadpack.

import scipy.integrate
scipy.integrate.quad(lambda x: 4.0/(1+x*x), 0, 1)
"""

from numpy import arange

# default # of rectangles
n = 20000

integration_points = (arange(1,n+1)-0.5)/n

def f(x):
    return 4.0/(1.0+x*x)

#from pyina.mpi_scatter import parallel_map
from pyina.mpi_pool import parallel_map


if __name__ == '__main__':

    out = parallel_map(f, integration_points)
    
    from pyina import mpi
    if mpi.world.rank == 0:
        print("approxmiate pi : ", sum(out)/n)
        print("calculated on %d nodes " % mpi.world.size)


# end of file
