import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import figure

df = pd.read_csv("noaadata.csv")
df.set_index('Year',inplace=True)
plt.rcParams.update({'font.size': 16})
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Montserrat'

figure(num=None, figsize=(20, 120), dpi=160, facecolor='w', edgecolor='k')
cmap = plt.get_cmap('seismic')
p1 = sns.heatmap(df,fmt=".3",cmap=cmap,annot=True,cbar=False)
p1.tick_params(right=True, top=True, labelright=True, labeltop=True)
p1.set_title('Global monthly temperature anomaly (relative to 1901-2000 average)\n(Data: NOAA; Credit: @timinclimate)\n')
plt.savefig('images/heatmapnoaa.png')
