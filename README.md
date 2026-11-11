# A correlation-scaled independence approximation for fork-join queues with general service times: a preregistered evaluation

An approximation for the mean response time of fork-join queues with general service times, tested once.

**Paper:** [paper.pdf](paper.pdf) · **Page:** [singularitysd.com/research/fork-join.html](https://singularitysd.com/research/fork-join.html) · Preprint, not yet peer reviewed.

## Abstract

The mean response time of a fork-join queue with $K\ge3$ parallel FCFS servers has no known closed form. The approximations in common use either assume exponential service (Nelson–Tantawi, Varma–Makowski) or rely only on the first two moments of the single-queue response time (the extreme-value approximation). We propose \[ T_K\approx R+\phi (R^{\max}_K-R),\qquad \phi=(1-r)^{\rho h},\qquad r=\frac{1}{1+c^2}, \] where $R$ is the exact M/G/1 mean response time and $R^{\max}_K$ is the classical upper bound: the exact mean of the maximum of $K$ independent M/G/1 response times, obtained from the Pollaczek–Khinchine transform by FFT. The factor $\phi$ accounts for the positive correlation that arrivals induce among the servers. Here $c^2$ is the squared coefficient of variation of service, and $h$ is a five-parameter function of $\rho$, $r$ and $\sqrt{\ln K}$. The functional form was found in an exploration phase in which a Kolmogorov–Arnold network suggested the $\sqrt{\ln K}$ dependence. It was then tested once, in a preregistered confirmation on simulated data that was not used to choose or fit it. \begin{itemize} \item **Exponential service**, $K\le128$: the maximum error is $1.03\%$, against $3.23\%$ for Nelson–Tantawi and $10.98\%$ for Varma–Makowski. \item **Service families never seen in calibration:** errors of $1.2$–$2.4\%$ for gamma, hyperexponential and Weibull service. The approximation fails, however, for lognormal ($\approx10\%$) and uniform ($34\%$) service, so the preregistered $5\%$ accuracy target for unseen families was *not* met. \end{itemize} We report both outcomes and analyse the failure.

## How it was made

The plan of the test was fixed before looking at the confirmation data, and the test was run once.

## What is in this repository

| file | what it is |
|---|---|
| `code/` | full code, protocol and intermediate results |
| `fig_errors.png` | figure |
| `main.tex` | LaTeX source of the paper |
| `paper.pdf` | the paper |

## Reproduce

The scripts in `code/` reproduce the numbers of the paper; each one explains at the top how to run it.

## Cite

```bibtex
@misc{singularity_fork_join_queues_2026,
  title  = {A correlation-scaled independence approximation for fork-join queues with general service times: a preregistered evaluation},
  author = {Singularity},
  year   = {2026},
  url    = {https://github.com/singularity-sd/fork-join-queues}
}
```

## License

Code: MIT (`LICENSE`). Paper, text and figures: CC BY 4.0 (`LICENSE-paper.md`). Third-party data keep their own licence where stated.

---

Part of [Singularity](https://singularitysd.com): forecasting where science goes next, then testing it.
