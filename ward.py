import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

data = pd.read_excel('Data.xlsx', index_col = 0)
data.fillna(0, inplace=True)

data_norm = (data - data.mean())/ data.std()
dist_matrix = linkage(data_norm, 'ward')

plt.figure(figsize = (10, 7))
plt.title("Metoda Warda")
dend = dendrogram(dist_matrix, labels = data.index, orientation = 'right')
plt.show()