import argparse
import pandas as pd
import numpy as np
from scipy.optimize import minimize_scalar


def nlog_likelihood(beta, counts):
    """log-likelihood function"""
    likelihood = - np.sum(np.log((1/counts)**(beta - 1)
                          - (1/(counts + 1))**(beta - 1)))
    return likelihood


def get_power_law_params(word_counts):
    """Get the power law parameters."""
    mle = minimize_scalar(nlog_likelihood,
                          bracket=(1+1e-10, 4),
                          args=word_counts,
                          method='brent')
    beta = mle.x
    alpha = 1 / (beta - 1)
    return alpha


def plot_fit(curve_xmin, curve_xmax, max_rank, alpha, ax):
    """Plot the power law curve that was fitted to the data."""
    xvals = np.arange(curve_xmin, curve_xmax)
    yvals = max_rank * (xvals**(-1/alpha))
    ax.loglog(xvals, yvals, color='grey')


def plot(args):
    df = pd.read_csv(args.inputs, header=None,
                     names=('word', 'word_counts'))
    df['rank'] = df['word_counts'].rank(ascending=False,
                                        method='max')
    ax = df.plot.scatter(x='word_counts', y='rank',
                         figsize=[12, 6], xlim=args.xlim,
                         grid=True, loglog=True)

    word_counts = df['word_counts'].to_numpy()
    alpha = get_power_law_params(word_counts)
    print(alpha)

    constant = df['word'].nunique()
    curve_xmin = df['word_counts'].min()
    curve_xmax = df['word_counts'].max()
    plot_fit(curve_xmin, curve_xmax, constant, alpha, ax)
    ax.figure.savefig(args.outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", type=argparse.FileType('r'),
                        nargs='?', default='-')
    parser.add_argument("--outfile", type=str, default='plotcounts.png')
    parser.add_argument("--xlim", type=float,
                        nargs=2, metavar=('XMIN', 'XMAX'))
    args = parser.parse_args()
    plot(args)
