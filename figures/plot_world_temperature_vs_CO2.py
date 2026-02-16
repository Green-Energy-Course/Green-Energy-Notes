# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 16:32:02 2026

@author: Scott
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt


plt.close("all")

temperature_df = pd.read_csv(
    "average-monthly-surface-temperature.csv"
)
year_list = []
T_list = []
T_year_list = []
y = 0

for day, T in zip(temperature_df["Day"], temperature_df["Monthly average"]):
    year = int(day[:4])
    if not year == y:
        if T_year_list:
            # print(len(T_year_list)) # sanity check. always 12.
            T_list.append(np.mean(T_year_list))
            year_list.append(y)
            T_year_list = []
        y = year
    T_year_list.append(T)

year_vec_1 = np.array(year_list)
T_vec_1 = np.array(T_list)

fig_1, ax_1 = plt.subplots()

ax_1.plot(year_vec_1, T_vec_1)
# so far so good :)


CO2_df = pd.read_csv(
    "co2-long-term-concentration.csv"
)
year_vec_2 = CO2_df["Year"].to_numpy()
c_vec_2 = CO2_df["Annual average"].to_numpy()

fig_2, ax_2 = plt.subplots()
ax_2.plot(year_vec_2, c_vec_2)

year_vec = np.array(list(set(year_vec_1) & set(year_vec_2)))
year_vec.sort()


cmap = mpl.colormaps["cool"]

fig, ax = plt.subplots()
ax.set_xlabel("CO2 concentration / [ppm]")
ax.set_ylabel("Global mean surface temperature / [$^\circ$C]")
norm = mpl.colors.Normalize(vmin=min(year_vec), vmax=max(year_vec))

ppm_list = []
T_list = []

for y in year_vec:
    ppm_y = np.interp(y, year_vec_2, c_vec_2)
    T_y = np.interp(y, year_vec_1, T_vec_1)
    ppm_list.append(ppm_y)
    T_list.append(T_y)
    ax.plot(ppm_y, T_y, "o", color=cmap(norm(y)))


ppm_vec = np.array(ppm_list)
T_vec = np.array(T_list)


ax.annotate(xy=(ppm_vec[-1], T_vec[-1]), text=str(year_vec[-1]))

cbar = fig.colorbar(mpl.cm.ScalarMappable(norm, cmap), ax=ax)
cbar.set_label("year")

fit = np.polyfit(ppm_vec, T_vec, deg=1)

ppm_mod = np.array([min(ppm_vec), max(ppm_vec)])
T_mod = fit[1] + fit[0] * ppm_mod

ax.plot(ppm_mod, T_mod, "k--")

fig.savefig("T_vs_CO2_concentration.svg")
