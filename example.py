import os
wc = r'C:\Users\colburm\OneDrive - Schroders\PD_package\new_package'
os.chdir(wc)


import merton_pds.merton_pds as pds
import pandas as pd
from matplotlib import pyplot as plt 

df = pd.read_excel(wc + '\data.xlsx',index_col=0)
rate = 0.05


output = pds.merton_pds(df.iloc[:,0].values*10**6, df.iloc[:,1].values*10**3, rate)
pds = pd.DataFrame(output[0], df.index)
plt.plot(pds)
