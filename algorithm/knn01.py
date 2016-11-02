# encoding: utf-8
from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.neighbors import KDTree
from sklearn.neighbors.nearest_centroid import NearestCentroid

x = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(x)

# 距离， 索引
distances, indices = nbrs.kneighbors(x)
print distances
print indices

print nbrs.kneighbors_graph(x).toarray()

kdt = KDTree(x, leaf_size=30, metric='euclidean')
print kdt.query(x, k=2, return_distance=False)

y = np.array([1, 5, 1, 2, -1, 1])
clf = NearestCentroid()
print x
clf.fit(x, y)

print clf.predict([[1, 1]])