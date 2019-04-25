def kmeans():
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('Clustering_small.csv')
    X = dataset.iloc[:, [2, 3]].values

    from sklearn.cluster import KMeans

    # Fitting K-Means to the dataset
    kmeans = KMeans(n_clusters=10, init = 'k-means++', random_state=42)
    y_kmeans = kmeans.fit_predict(X)

    # Visualising the clusters
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s =20, c = 'red', label = 'Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s =20, c = 'blue', label = 'Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s =20, c = 'green', label = 'Cluster 3')
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s =20, c = 'cyan', label = 'Cluster 4')
    plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s =20, c = 'purple', label = 'Cluster 5')
    plt.scatter(X[y_kmeans == 5, 0], X[y_kmeans == 5, 1], s =20, c = '#84fff2', label = 'Cluster 6')
    plt.scatter(X[y_kmeans == 6, 0], X[y_kmeans == 6, 1], s =20, c = '#7c7c7c', label = 'Cluster 7')
    plt.scatter(X[y_kmeans == 7, 0], X[y_kmeans == 7, 1], s=20, c = '#ff7130', label = 'Cluster 8')
    plt.scatter(X[y_kmeans == 8, 0], X[y_kmeans == 8, 1], s=20, c = '#ff72fa', label = 'Cluster 9')
    plt.scatter(X[y_kmeans == 9, 0], X[y_kmeans == 9, 1], s =20, c = 'magenta', label = 'Cluster 10')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=60, c='black', label='Centroids')
    plt.title('Clusters of packets')
    plt.xlabel('Throughput')
    plt.ylabel('Buffer_size')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    kmeans()
