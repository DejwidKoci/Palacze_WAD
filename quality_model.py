from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
import numpy as np
import pandas as pd
 
df = pd.read_excel('Data.xlsx')

df.fillna(0, inplace=True)

Y = df['Country']
X = df.drop(columns=['Country'])

 
# K-Means
kmeans = KMeans(n_clusters = 30, random_state = 1).fit(X)

# for n = 30 measure is the highest
 
# we store the cluster labels
labels = kmeans.labels_
 
print(metrics.calinski_harabasz_score(X, labels))