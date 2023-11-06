import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Wczytaj dane
df = pd.read_excel('Data.xlsx')

X = df.select_dtypes(include=['float', 'int'])
X = X.fillna(0)  


k = 3  # Dostosuj liczbę klastrów do swoich potrzeb
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Przypisanie każdego kraju do klastra
df['Cluster'] = kmeans.labels_

print(df[['Country', 'Cluster']])

# Redukcja do 2D do stworzenia wykresu
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c = kmeans.labels_, cmap = 'viridis')
plt.title('Klasteryzacja k-średnich')
plt.show()
