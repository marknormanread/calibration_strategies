# Corresponds to Figure 1C
#
# Mark N. Read, 2018

import numpy as np
import seaborn as sns
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import matplotlib.pyplot as plt
import scipy.stats as ss


target = np.random.normal(0, 3, size=500)

samples = np.arange(5, 500)
ds = []
ps = []
dist = list(np.random.normal(1, 3, size=min(samples)))
for sample_size in samples:
    print('processing sample size ' + str(sample_size))
    d, p = ss.ks_2samp(target, dist)
    ds.append(d)
    ps.append(p)
    new_sample = np.random.normal(1, 3, size=1)
    dist.append(new_sample)

sns.set_style("darkgrid")
rcParams.update({'font.size': 12})

fig = plt.figure(figsize=(6, 3))
ax = fig.gca()
ax.plot(samples, ps, 'b-')
ax.set_ylabel('P value', color='b')
ax.tick_params('y', colors='b')
ax.set_yscale('log')
plt.ylim((min(ps), 1))

ax2 = ax.twinx()
ax2.plot(samples, ds, 'r-')
ax2.set_ylabel('KS D', color='r')
ax2.tick_params('y', colors='r')
ax2.set_ylim((0, 1))
ax2.grid(b=False)

ax.set_xlabel('Sample size')

# plt.show()
plt.savefig("convergence.png", dpi=600)