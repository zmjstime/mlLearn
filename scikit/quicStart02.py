# Unless otherwise specified, input will be cast to float64:

import numpy as np
from sklearn import random_projection
from sklearn import datasets
from sklearn.svm import SVC

rng = np.random.RandomState(0)
xx = rng.rand(10, 2000)
xx = np.array(xx, dtype='float32')
print xx.dtype

transformer = random_projection.GaussianRandomProjection()
x_new = transformer.fit_transform(xx)
print x_new.dtype


iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)

print list(clf.predict(iris.data[:3]))

clf.fit(iris.data, iris.target_names[iris.target]) 
print list(clf.predict(iris.data[:3]))

X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)

clf.set_params(kernel='linear').fit(X, y)  
print clf.predict(X_test)

clf.set_params(kernel='rbf').fit(X, y)  
print clf.predict(X_test)
