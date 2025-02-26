import os
import pandas as pd
import matplotlib.pyplot as plt

currnet_path = os.path.dirname(__file__)

income_csv = os.path.join(currnet_path, 'ddf--entities--income_group.csv')
income = pd.read_csv(income_csv)

print(income.head())

exit()

# plot the income distribution
fig = plt.figure()

for i, row in income.iterrows():
    plt.bar(row['name'], row['income_group'])

plt.xlabel('Country')
plt.ylabel('Income Group')
plt.show()
