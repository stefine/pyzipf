import argparse
from matplotlib.pyplot import loglog, xlim
import pandas as pd


def plot(args):
    df = pd.read_csv(args.inputs, header=None,
                     names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                           method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency', y='rank',
                               figsize=[12, 6], xlim=args.xlim,
                               grid=True, loglog=True)
    fig = scatplot.get_figure()
    fig.savefig(args.outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", type=argparse.FileType('r'),
                        nargs='?', default='-')
    parser.add_argument("--outfile", type=str, default='plotcounts.png')
    parser.add_argument("--xlim", type=float,
                        nargs=2, metavar=('XMIN', 'XMAX'))
    args = parser.parse_args()
    plot(args)
