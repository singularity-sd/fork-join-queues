"""Correlation-scaled independence approximation for the mean response time of a homogeneous fork-join queue
(Poisson arrivals, K FCFS servers, general service with mean 1).

    T_K ~= R + phi * (Rmax_K - R),  phi = (1 - r)^(rho*h),  r = 1/(1 + c2),
    h = a0 + a1 r + a2 rho + (b0 + b1 rho) sqrt(ln K)

R: exact M/G/1 mean response time; Rmax_K: mean of the maximum of K independent M/G/1 response times
(Pollaczek-Khinchine transform evaluated by FFT). Pass the service CDF F (mean must be 1) and c2.
Validated on exponential-type tails (gamma, hyperexponential, Weibull); NOT reliable for bounded (uniform) or
lognormal service (see paper).
"""

import math

import numpy as np

A0, A1, A2, B0, B1 = 0.020780, 0.089624, 0.229206, 0.359879, -0.205055


def sojourn_cdf(F, c2, rho, n=2 ** 20):
    ew = rho * (1 + c2) / (2 * (1 - rho))
    xmax = max(60.0, 40 * (ew + 1) * (1 + math.sqrt(c2)))
    x = np.linspace(0, xmax, n, endpoint=False)
    dx = x[1] - x[0]
    ps = np.diff(np.r_[0.0, F(x + dx)])
    pe = (1 - F(x + dx / 2)) * dx
    pe /= pe.sum()
    m = 2 * n
    ft = (1 - rho) / (1 - rho * np.fft.rfft(pe, m)) * np.fft.rfft(ps, m)
    return x + dx, np.clip(np.cumsum(np.fft.irfft(ft, m)[:n]), 0, 1)


def response_time(F, c2, rho, K):
    x, Ft = sojourn_cdf(F, c2, rho)
    dx = x[1] - x[0]
    R = float(np.sum(1 - Ft) * dx)
    if K == 1:
        return R
    rmax = float(np.sum(1 - Ft ** K) * dx)
    r = 1 / (1 + c2)
    h = A0 + A1 * r + A2 * rho + (B0 + B1 * rho) * math.sqrt(math.log(K))
    return R + (1 - r) ** (rho * h) * (rmax - R)


if __name__ == "__main__":
    expo = lambda x: 1 - np.exp(-x)
    for rho in (0.3, 0.7):
        print(f"exponential, rho={rho}, K=16: {response_time(expo, 1.0, rho, 16):.4f}")
