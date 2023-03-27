import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import fsolve
from matplotlib import pyplot as plt 

def merton_pds(equity, liability, rate, **kwargs):
    # Argument check
    maturity = kwargs.get('Maturity', 1)
    drift = kwargs.get('Drift', rate)
    num_periods = kwargs.get('NumPeriods', 250)
    tolerance = kwargs.get('Tolerance', 1e-6)
    max_iterations = kwargs.get('MaxIterations', 500)
    
    # Compute the value of the assets
    A, Sa = TS_Solver(equity, liability, rate, maturity, tolerance, num_periods, max_iterations)
    # Compute the Distance-to-Default and Probability of Default
    DD = (np.log(A/liability) + (drift - 0.5*Sa**2)*maturity)/(Sa*np.sqrt(maturity))
    PD = 1 - norm.cdf(DD)
    #[PD, DD, A, Sa]
    return PD, DD, A, Sa

import numpy as np

def TS_Solver(E, D, r, T, Tol, NumPeriods, MaxIterations):
    # Helper function that solves for the time series version of the Merton
    # model using an iterative approach. Returns the asset (A) and asset 
    # volatility (Sa) values.
    
    # Iter 0: Define the time step and initial guess of debt and asset 
    #         values
    N = len(D)
    A = E + D * np.exp(-r*T)
    LogReturnsA = np.log(A[1:] / A[:-1])
    Sa = np.sqrt(NumPeriods) * np.sqrt((1/(N-2)) * np.sum((LogReturnsA-np.mean(LogReturnsA))**2))

    # Iter 1
    N1, N2, Disc = getNormcdfs(A, Sa, D, r, T)
    D1 = A * (1-N1) + D * Disc * N2
    
    # Define the error, the value of which needs to be minimized for
    # convergence
    Aold = A
    A = E + D1
    Error = np.linalg.norm(A-Aold)/np.sqrt(N)
    Count = 1
    
    # Iterate until error falls below the tolerance
    while (Error > Tol) and (Count < MaxIterations):
        N1, N2, Disc = getNormcdfs(A, Sa, D, r, T)
        D_ = A * (1-N1) + D * Disc * N2
        Aold = A
        A = E + D_
        LogReturnsA = np.log(A[1:] / A[:-1])
        Sa = np.sqrt(NumPeriods) * np.sqrt((1/(N-2)) * np.sum((LogReturnsA-np.mean(LogReturnsA))**2))
        Error = np.linalg.norm(A-Aold)/np.sqrt(N)
        Count = Count + 1
    
    # Issue a warning if convergence did not happen
    if (Count >= MaxIterations):
        if (Error > Tol):
            print('NonConvergence')
    
    return A, Sa


def getNormcdfs(A, Sa, D, r, t):
    # Returns the evaluation of the normal cumulative distribution function 
    # at the parameters "d1" and "d2", defined below, as well as the
    # discount factor for the liabilities.
    
    RootT = np.sqrt(t)
    d1 = (np.log(A/D) + (r + (Sa**2)/2)*t) / (Sa*RootT)
    d2 = d1 - Sa*RootT
    
    N1 = norm.cdf(d1)
    N2 = norm.cdf(d2)
    Disc = np.exp(-r*t)
    
    return N1, N2, Disc



