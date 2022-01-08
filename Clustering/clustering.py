# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

biased_dataset = pd.read_csv('testingcluster.csv')

# Defining the scatterplot drawing function
def draw_scatterplot(x_data, x_label, y_data, y_label):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.scatter(x_data, y_data, s=30)
    plt.show()
# Plot the scatterplot
draw_scatterplot(biased_dataset['avg_Phone_rating'],'Phone', biased_dataset['avg_TV_rating'], 'TV')

# Let's turn our dataset into a list
X = biased_dataset[['avg_Phone_rating','avg_TV_rating']].values
# Import KMeans
from sklearn.cluster import KMeans
# Create an instance of KMeans to find two clusters
kmeans_1 = KMeans(n_clusters=3)
# Use fit_predict to cluster the dataset
predictions = kmeans_1.fit_predict(X)
# Defining the cluster plotting function
def draw_clusters(biased_dataset, predictions, cmap='viridis'):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    ax.set_xlabel('Avg Phone rating')
    ax.set_ylabel('Avg TV rating')
    clustered = pd.concat([biased_dataset.reset_index(), pd.DataFrame({'group':predictions})], axis=1)
    plt.scatter(clustered['avg_Phone_rating'], clustered['avg_TV_rating'], c=clustered['group'], s=20, cmap=cmap)
    plt.show()
# Plot
draw_clusters(biased_dataset, predictions)