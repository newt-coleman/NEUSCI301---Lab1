import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat

nostim = np.array([0.8603, 0.7082, 8.8652, 10.2361, 4.7214, 4.9091, 2.0628, 1.8917, 3.4381])
blowstim = np.array([7.9418, 4.1175])
upstim = np.array([113.1542, 64.3984, 68.0802])
downstim = np.array([56.1283, 50.9151])

cats = np.array([1,1,1,1,1,1,1,1,1,2,2,3,3,3,4,4])#haha this is so bad please find a better way

plt.rcParams['font.size'] = 15
fig, ax = plt.subplots()
ax.scatter(np.ones(len(nostim)), nostim)          ### Raw data points
ax.scatter(np.ones(len(blowstim))*1.75, blowstim)
ax.scatter(np.ones(len(upstim))*2.5, upstim)
ax.scatter(np.ones(len(downstim))*3.25, downstim)

ax.errorbar(1.15, np.mean(nostim), np.std(nostim), fmt='o', linewidth=2, capsize=6) ## with stats
ax.errorbar(1.9, np.mean(blowstim), np.std(blowstim), fmt='o', linewidth=2, capsize=6)
ax.errorbar(2.65, np.mean(upstim), np.std(upstim), fmt='o', linewidth=2, capsize=6)
ax.errorbar(3.4, np.mean(downstim), np.std(downstim), fmt='o', linewidth=2, capsize=6)

plt.ylabel('Spikes/sec')                          ### Make fig readable/pretty
ax.set_xticks([1,1.75,2.5,3.25], ['No stimulation', 'Blowing', 'Up stroke', 'Down stroke'])


print("Mean no: " + str(np.mean(nostim)) + "\nStd: " + str(np.std(nostim)))        ## give me the stats
print("Mean blow: " + str(np.mean(blowstim)) + "\nStd: " + str(np.std(blowstim)))
print("Mean up: " + str(np.mean(upstim)) + "\nStd: " + str(np.std(upstim)))
print("Mean down: " + str(np.mean(downstim)) + "\nStd: " + str(np.std(downstim)))


# plt.show()
