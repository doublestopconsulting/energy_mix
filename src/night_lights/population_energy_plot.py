import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter



df_e = pd.read_csv('../../data/derived/state_year_total_e.csv')
df_pop = pd.read_csv('../../data/other/us_population.csv')


df_e = df_e[df_e.StateCode=='US']
df_e.rename(columns={'Data': 'billion BTU'}, inplace=True)


# dual y-axes
fig, ax1 = plt.subplots(figsize=(12,8), layout="constrained")
ax1.set_xlabel('Year', fontsize=15)
ax1.set_ylabel('Energy consumed [billions BTU]', color = 'black', fontsize=15)
ax1_plot = ax1.plot(df_e['Year'], df_e['billion BTU'], color = 'black',
                    label = 'Energy consumed [billions BTU]', marker='.',
                    markersize=9)
_, max_e = ax1.get_ylim()
ax1.set_ylim([0, max_e])
ax1.tick_params(axis='both', labelcolor= 'black', labelsize=11)
ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))

ax2=ax1.twinx()
ax2.set_ylabel('Population', color = 'blue', fontsize=15)
ax2_plot = ax2.plot(df_pop['Year'], df_pop['US_Population'], color = 'blue',
                    label = 'US Population')
ax2.tick_params(axis='y', labelcolor='blue', labelsize=11)
_, max_pop = ax2.get_ylim()
ax2.set_ylim([0, max_pop])
ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))


all_the_plots = ax1_plot+ax2_plot
labels = [plot.get_label() for plot in all_the_plots]
ax1.legend(all_the_plots, labels, fontsize=12)

ax1.grid(axis='x', which='major')

plt.title('Energy Consumed & Population in the US, 1960 - 2023', fontsize=18)
# plt.show()

plt.savefig('US_energy_and_population.png')




# # using subplots
# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,8))

# df_e.plot(ax=ax1, x='Year', y='billion BTU', legend='Energy [billion BTU]')

# _, max_e = ax1.get_ylim()
# ax1.set_ylim([0, max_e])

# df_pop.plot(ax=ax2, x='Year', y='US_Population', legend='US Population')
# _, max_pop = ax2.get_ylim()
# ax2.set_ylim([0, max_pop])

# plt.show()