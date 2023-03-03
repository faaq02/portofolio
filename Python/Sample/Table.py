import matplotlib.pyplot as plt

labels = ['comp', 'mgt','comm', 'acs', 'vcd']

men_means = [20,35,30,35,27]
women_means = [25,32,34,20,25]

men_std = [2, 3, 4, 1, 2]
women_std = [3,5,2,3,3]

width = 0.35

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='women')

ax.set_ylabel('scores')

ax.set_title('scores by major and gender')

ax.legend()

plt.show()