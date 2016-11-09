from sklearn import svm
from sklearn import datasets
import pickle


clf = svm.SVC()
iris = datasets.load_iris()

x, y = iris.data, iris.target

clf.fit(x, y)
# print clf.predict(x[:1])

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print clf2.predict(x[0:1])
