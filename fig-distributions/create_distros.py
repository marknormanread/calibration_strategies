# Corresponds to Figure 1A
#
# Mark N. Read, 2018

import numpy.random
import seaborn as sns
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import matplotlib.pyplot as plt
import scipy.stats as ss


sns.set_style("darkgrid")
rcParams.update({'font.size': 12})


def perform_stats(target, model, name, f):
    d, p = ss.ks_2samp(target, model)
    f.write('\n')
    f.write(name)
    f.write('\n\n')
    f.write('KS D={:.2f}, p={:.2f}\n'.format(d, p))

    t, p = ss.ttest_ind(target, model)
    f.write('T test t={:.2f}, p={:.2f}\n'.format(t, p))

    u, p = ss.mannwhitneyu(target, model, alternative='two-sided')
    f.write('MannWhitney U U={:.2f}, p={:.2f}\n'.format(u, p))
    f.write('\n')


def plot_distro(dist, name, colour, xrange, xticks=True):
    plt.clf()
    plt.figure(figsize=(4, 2))
    sns.distplot(dist, hist=True, color=colour, norm_hist=False)
    plt.xlim(xrange)
    plt.axes().set_yticks([])
    if not xticks:
        plt.axes().set_xticks([])
    plt.savefig(name, dpi=300)


f = open('distributions_contrasted.txt', 'w')
samples = 1000
target = numpy.random.normal(0.0, 3.0, samples)


s1 = numpy.random.normal(0.0, 3.0, samples)
perform_stats(target, s1, 'same', f)

s2 = numpy.random.normal(3.0, 3.0, samples)
perform_stats(target, s2, 'shifted mean', f)

s3 = numpy.random.normal(0.0, 6.0, samples)
perform_stats(target, s3, 'shifted distro', f)

combined = numpy.concatenate((target, s1, s2, s3))
xmin = numpy.min(combined)
xmax = numpy.max(combined)
xrange = (xmin, xmax)


cols = sns.color_palette("hls", 4)
plot_distro(target, 'target.png', cols[0], xrange, xticks=True)
plot_distro(s1, 'identical.png', cols[1], xrange, xticks=True)
plot_distro(s2, 'shifted_mean.png', cols[2], xrange, xticks=True)
plot_distro(s3, '2x_variance.png', cols[3], xrange, xticks=True)
f.close()
