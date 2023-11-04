<h1 align="center">
  Clustering
</h1>

---

1. Clustering.
    - This is Unsupervised Technique.
    - Basically group or cluster the data of similar kind.
    - Unsupervised algorithms:
        1. K Means Clustering.
        2. Hiearichal Clustering.
        3. DBSCAN Clustering.
        4. Silhoutte Clustering.

---

2. K Means Clustering.
    - Steps :
        1. Intialize some k Value(Number of clusters).
        2. Find out the points nearest to centroid and group them.
        3. Calculate the average distance and move centroid.
        4. Repeat Step 2 and Step 3 until Centroid is placed correctly.
    - How to select the K value ?
        - WCSS = Within Cluster Sum of Squares
        - WCSS = $\sum_{i = 1}^n$(distance of points to nearest centroid)
        - We Polt a graph K value v/s WCSS 
            - Using Elbow Method the point after which we have the stabilization is the k value.
            - above k value there will be abrupt change in the WCSS value.
    - Distance Calculation
        1. Eucledian Distance.
            - Formula 
            $$distance = \sqrt{(x_{2} - x_{1})^2 + (y_{2} - y_{1})^2}$$
        2. Manhatten Distance.
            - Formula 
            $$distance = |x_{2} - x_{1}| + |y_{2} - y_{1}|$$
    - Random intialization trap[K Means ++]
        - When we do random intialization of point to make the cluster there is possibility of getting a wrong cluster of the randomly intialized points are close to each other and other point is far.
        - Solution is We have to make sure that the randomly intialized points are at maximum distance enough to avoid the wrong clustering.

---

3. Hierarchical Clustering.
    - Here, There will be no centroid.
    - 2 Types of Hierarchical Clustering.
        1. Agglomerative.
        2. Divisive.
        - They are opposite to each other.
        - Agglomerative is bottom up approch in dendogram.
        - Divisive is top down approch in dendogram.
    - Step for Agglomerative to form clusters.
        1. For each point we consider as single clustering.
        2. Cluster the nearest points and create a new cluster.
        3. Repeat clustering nearest clusters until we get a single cluster.
    - Dendogram to find the value of K.
        - For agglomerative we do clustering with points with less eucledian distance.
        - Now, we find the K Value by finding number of intercept of the horizontal line.
        - We have to draw the horizontal line so the minimum vertical line intercept the horizontal line.
        - Note : If we decrease the Eucledian distance value then there will be increase in number of clusters.

---

4. Difference between K Means and Hierarchial Clustering.
    1. Dataset size.
        - K Means = for large dataset.
        - Hierarchial = for small dataset as form dendogram become difficult to find the value of k.
    2. Type of Data.
        - K Means = for numerical data.
        - Hierarchial = variety of data.
    3. Forming cluster.
        - K Means = Difficult to find K Value(number of clusters) because to find the stabilization point in Elbow method becomes difficult.
        - Hierarchial = Easy to find K Value.

---

5. DBSCAN Clustering.
    - Here we have 3 types of points:
        - There are 2 parameter = minimum points tells min number which should be present in he cluster and $\epsilon$ which represent the radius of the cluster.
        1. Core point.
            - Number of points within $\epsilon$ will be greater than the minimum points the that $\epsilon$ point is considered as the Core point.
        2. Border point.
            - Number of points within $\epsilon$ will be less than the minimum points the that $\epsilon$ point is considered as the Border point.
        3. Outlier or Noise. 
            - Number of points within $\epsilon$ = 1 which is the $\epsilon$ point is considered as the Outlier point.
    - DBSCAN Can handle the non linear data and also Noise present in dataset.

--- 

6. Silhouette Clustering.
    - Used to Validate the K Value found in Elbow Method.
    - Steps to find Silhouette Score.
        1. Find the average distance from a point within the cluster(i) which is considered as a(i).
        $$a(i) = \frac{1}{|C_{i}|-1} \sum_{j \in C_{i} and i != j}d(i,j)$$
        2. Find the average distance from a point of cluster(i) to all points in the cluster(j) which is considered as b(i).
        $$b(i) = \frac{1}{|C_{j}|} \sum_{j \in C_{j}}d(i,j)$$
        3. Calculate Silhoutte Score.
        $$s(i) = \frac{b(i) - a(i)}{max[a(i),b(i)]}$$
    - Silhoutte score range between 0 to 1.
    - If Silhoutte Score is near to 1 denotes that the clustering is done better. 

--- 

7. K Means Implementation.
    1. Create dataset.
        - ```from sklearn.datasets import make_blobs```
        - ```x, y = make_blobs(n_samples = 1000, centers = 3, n_features = 2, random_state = 23)```
    2. Train Test Split
        - ```form sklearn.model_selection import trian_test_split```
        - ```x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)```
    3. Manually Finding K Value using Elbow Method
        - ```from sklearn.cluster import KMeans```
        - Find wcss for 1 to 10 values(k)
        - ```kmeans = KMeans(n_clusters = k, init = 'k-means++')``` = k is a loop variable and k-means++ make sure that centroids are at max distance enough.
        - ```kmeans.fit(x_train)``` 
        - ```kmeans.inertia_``` = gives the wcss value.
        - plot the Elbow Curve.
            - ```plt.plot(range(1,11), wcss)```
            - ```plt.xticks(range(1,11))```
        - Manually Select the K Value from Graph - select the point for where the line get stabilization.
    4. Automatically find the K value (elbow) using knee locator method.
        - ```!pip install kneed```
        - ```from kneed import KneeLocator```
        - ```knee = KneeLocator(range(1,11), wcss, curve = 'convex', direction = 'decreasing')```
        - ```knee.elbow``` - Give the point at which the stablization takes places.
    5. Clustering.
        - ```kmeans = KMeans(n_clusters = k, init = 'k-means++')``` = repalce the k by the value found in above methods.
        - ```kmeans.fit(x_train)```
        - ```kmeans.labels_``` = gives array which tells in which category the training data falls.
        - plot and see the cluster formed.
        - plot and observe the clusters
            - ```plt.scatter(x_train[:,0], x_train[:,1], c = kmeans.labels_)``` -  we can see the k number of cluster.
    6. Validate the K Value using silhouette value.
        - ```from sklearn.metrics import silhouette_score```
        - ```score = silhouette_score(x_train, kmeans.labels_)``` - find for different k values and add to the a list.
        - plot the graph
            - ```plt.plot(range(2,11),silhouette_coefficients)```
            - ```plt.xticks(range(1,11))```
            - In the graph the pickest point is the k value which do the better clustering.

--- 

8. Hierarchical Clustering Implementation.
    1. Load dataset and consider the independent features only.
    2. Standardization.
        - ```from sklearn.preprocessing import StandardScaler```
        - ```scaler = StandardScaler()```
        - ```x_scaled = scaler.fit_transform(x)```
    3. Dimensionality reduction - PCA.
        - ```from sklearn.decomposition import PCA```
        - ```pca = PCA(n_components = 2)``` - converting into 2D
        - ```pca_scaled = pca.fit_transform(x_scaled)```
        - Visualize the data to see clusters present 
            - ```plt.scatter(pca_scaled[:,0], pca_scaled[:,1])``` 
    4. Manually finding the K value using Dendogram.
        - ```import scipy.cluster.hierarchy as sc```
        - ```sc.dendrogram(sc.linkage(pca_scaled, method = 'ward'))```
        - Find the longest vertical line which donot intercept with any other any horizontal line.
    5. Clustering.
        - ```from sklearn.cluster import AgglomerativeClustering```
        - ```cluster = AgglomerativeClustering(n_clusters = 2, affinity = 'euclidean', linkage = 'ward')``` = n_clusters is obtained from the dendogram.
        - ```cluster.fit(pca_scaled)```        
        - plot and observe the clusters
            - ```plt.scatter(pca_scaled[:,0], pca_scaled[:,1], c = cluster.labels_)```
    6. Validate the K Value using silhouette value.
        - Same validation as of KMeans clustering.

--- 

9. DBSCAN Implementation.
    1. Create the dataset.
        - ```from sklearn.datasets import make_moons``` - gives the 2 interleaving half circles.
        - ```x, y = make_moons(n_samples = 250, noise = 0.12)``` = noise used to spread the values.
        - Visualize the data. 
            - ```plt.scatter(x[:,0],x[:,1])```
    2. Standardization.
        - ```from sklearn.preprocessing import StandardScaler```
        - ```scaler = StandardScaler()```
        - ```x_scaled = scaler.fit_transform(x)```
    3. Clustering.
        - ```from sklearn.cluster import DBSCAN```
        - ```dbscan = DBSCAN(eps = 0.3)```
        - ```dbscan.fit(x_scaled)```
        - In ```dbscan.labels_``` we can see some -1 values other than 0 and 1 those points are the outliers.
        - plot and observe the clusters
            - ```plt.scatter(x[:,0],x[:,1],c = dbscan.labels_)```

---
