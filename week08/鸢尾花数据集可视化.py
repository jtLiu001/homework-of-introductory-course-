import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

# 加载鸢尾花数据集
iris = load_iris()
iris_df = pd.DataFrame(data= iris['data'], columns= iris['feature_names'])
iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)


plt.figure(figsize=(10, 6))
sns.scatterplot(x='petal length (cm)', y='petal width (cm)', hue='species', data=iris_df)
plt.title('Iris Species - Petal length vs Petal width')
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(iris_df['sepal length (cm)'], kde=True, bins=30)
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal width (cm)', data=iris_df)
plt.title('Boxplot of Sepal Width for Different Iris Species')
plt.show()
