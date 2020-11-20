import geopandas
import pandas as pd
import matplotlib.style
import matplotlib as m
import matplotlib.pyplot as plt
import numpy as np

m.rcParams['figure.figsize'] = [14.0, 10.0]

croatia_counties = geopandas.read_file('counties.topojson')

covid = pd.read_excel('podaci_zupanije.xlsx')

#vmin, vmax = covid.select_dtypes(include=[np.number]).min().min()-10, 100
vmin, vmax = -100, 100
colormap = 'seismic'
j = len(covid.columns)-14
k = 1

for i in covid.columns[-7:]:

    croatia_counties['Data'] = covid[i][:]
    ax = croatia_counties.plot(column='Data', cmap=colormap, vmin=vmin, vmax=vmax)
    fig = ax.get_figure()
    cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
    sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    fig.colorbar(sm, cax=cax)
    ax.set_title(covid.columns[j]+': Tjedna promjena broja zaraženih (%)',size=18)
    fig.savefig('C:/Users/domagoj.sesar/Documents/Data/Python/Geopandas/Croatia/Covid19/Karta/{ime}.png'.format(ime=k))
    j = j + 1
    k = k + 1
