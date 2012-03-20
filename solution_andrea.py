from pprint import pprint
import itertools

PYRAMID = [range(1, 5)] * 9
CUBIC = [range(1, 7)] * 6

pyramid_combs = itertools.product(*PYRAMID)
cubic_combs = itertools.product(*CUBIC)

d_pyr = dict((i, 0) for i in range(9, 37))
d_cub = dict((i, 0) for i in range(6, 37))

for p in pyramid_combs:
    d_pyr[sum(p)] += 1

for p in cubic_combs:
    d_cub[sum(p)] += 1

pprint(d_cub)
pprint(d_pyr)

tot_cube = sum(d_pyr.values())

min_kc = min(d_cub)
prob = 0

for kp in sorted(d_pyr):
    greater = 0
    for kc in range(min_kc, kp):
        greater += d_cub[kc]

    prob += float(greater) / tot_cube


print(prob)

import matplotlib.pyplot as plt

ls_cub = []
for k, v in d_cub.items():
    ls_cub += [k] * v

ls_pyr = []
for k, v in d_pyr.items():
    ls_pyr += [k] * v

plt.title("cubic")
plt.hist(ls_cub, bins=range(36))
plt.show()

plt.title("pyramid")
plt.hist(ls_pyr, bins=range(36))
plt.show()
