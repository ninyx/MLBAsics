#Load and Train Iris DataSet from sklearn
from sklearn import datasets
from sklearn import tree

iris = datasets.load_iris()
print(iris.target_names)

#Training the model
classifier = tree.DecisionTreeClassifier()
classsifier = classifier.fit(iris.data, iris.target)

print(classifier.predict([[5.1,3.5,1.4,0.2]]))