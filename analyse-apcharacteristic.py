import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stat

dat = pd.read_csv("apshape.csv")
apshape = pd.DataFrame({'downstroke': dat['nadirt'] - dat['onset'],
                        'upstroke': dat['peakt'] - dat['nadirt'],
                        'repolarization': dat['end'] - dat['peakt'],
                        'length': dat['end'] - dat['onset'],
                        'depv': dat['hypv'],
                        'repv': dat['depv'],
                        'totalAmp': dat['hypv'] - dat['depv']})

depot = apshape['downstroke'] + (apshape['upstroke'] / 2)
repot = (apshape['upstroke']/2) + apshape['repolarization']

plt.rcParams['font.size'] = 16
fig, ax = plt.subplots()


# print(stat.ttest_rel(depot, repot))                                            ## phase timing stats + graphs
# print("Mean dep: " + str(np.mean(depot)) + "\nStd: " + str(np.std(depot)))
# print("Mean rep: " + str(np.mean(repot)) + "\nStd: " + str(np.std(repot)))
# ax.boxplot([depot, repot], tick_labels = ['Depolarization', 'Repolarization'])
# plt.ylabel('Phase timings (ms)')

print(stat.ttest_rel(apshape['repv'], abs(apshape['depv'])))
print("Mean dep: " + str(np.mean(apshape['depv'])) + "\nStd: " + str(np.std(apshape['depv'])))   ## phase amp stats
print("Mean rep: " + str(np.mean(apshape['repv'])) + "\nStd: " + str(np.std(apshape['repv'])))    # + graphs   
ax.boxplot([abs(apshape['depv']), apshape['repv']], tick_labels = ['Depolarization', 'Repolarization'])
plt.ylabel('Phase Amplitude (mV)')

ax.set_box_aspect(1)
plt.show()

