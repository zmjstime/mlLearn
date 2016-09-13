# -*- coding: utf-8 -*-
import numpy as np
from sklearn import neighbors
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

def getData():
	data = []
	labels = []
	with open('data1.txt') as dataFile:
	    for line in dataFile:
	        tokens = line.strip().split(' ')
	        data.append([float(tk) for tk in tokens[:-1]])
	        labels.append(tokens[-1])
	return np.array(data), np.array(labels)

x, labels = getData()
y = np.zeros(labels.shape)
y[labels == 'fat'] = 1


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

h = .01
x_min, x_max = x[:, 0].min() - 0.1, x[:, 0].max() + 0.1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))


clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train, y_train)

answer = clf.predict(x)
print x
print answer
print y
print np.mean(answer == y)

# precision, recall, thresholds = precision_recall_curve(y_train, clf.predict(x_train))
# answer = clf.predict_proba(x)[:,1]
# print classification_report(y, answer, target_names = ['thin', 'fat'])

''' 将整个测试空间的分类结果用不同颜色区分开'''
answer = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,1]
z = answer.reshape(xx.shape)
plt.contourf(xx, yy, z, cmap=plt.cm.Paired, alpha=0.8)

''' 绘制训练样本 '''
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=plt.cm.Paired)
plt.xlabel(u'身高')
plt.ylabel(u'体重')
plt.show()