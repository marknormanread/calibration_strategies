# Corresponds to Figure 1B
#
# Mark N. Read, 2018

import numpy.random
import seaborn as sns
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import matplotlib.pyplot as plt


sns.set_style("darkgrid")
rcParams.update({'font.size': 9})


target = numpy.random.normal(0, 3, size=500)

dist = numpy.random.normal(3, 3, size=500)


cols = sns.color_palette("hls", 4)
fig = plt.figure(figsize=(4, 2))
sns.distplot(target, kde_kws=dict(cumulative=True), hist=False, color=cols[0])
sns.distplot(dist, kde_kws=dict(cumulative=True), hist=False, color=cols[2])
plt.ylabel('Cumulative distribution')
# plt.show()
plt.savefig('ks_tutorial.png', dpi=300)
