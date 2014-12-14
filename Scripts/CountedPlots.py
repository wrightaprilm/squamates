import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import sys

data = pd.read_csv(sys.argv[1], header=None)
data.columns = ['A','B','C','D','E', 'F', 'G']
data

data=data.drop('A',axis=1)
data=data.drop('C',axis=1)
data=data.drop('E',axis=1)
data=data.drop('B',axis=1)

data['D'] = data['D'].astype(int)

table = pivot_table(data, index=['D'], columns=['G'])

table.plot(kind='bar',secondary_x=True, legend=False, width=.7)

plt.tight_layout()
plt.savefig('hist.svg', bbox_inches='tight', dpi=300)



