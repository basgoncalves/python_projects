
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) # for .py

fat = pd.read_csv(os.path.join(dir_path, 'SOCR-HeightWeight.csv'))
fat['brozek'] = np.random.randint(1, 50, fat.shape[0])
fat['siri'] = np.random.randint(1, 10, fat.shape[0])

plt.figure(figsize=(17,10))
plt.scatter(fat['Weight(Pounds)'], fat['Height(Inches)'], c=fat['brozek'],s=fat['siri']**2 , alpha=0.7,cmap = 'gnuplot2')
plt.title('Weight vs Height with color gradient representing Brozek',fontsize=25)
plt.xlabel('Weight', fontsize=20)
plt.ylabel('Height', fontsize=20)
plt.grid(True)
cb= plt.colorbar()
cb.set_label('Brozek', fontsize=20)
plt.show()