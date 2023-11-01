<h1 align="center">
  K-Nearest Neighbors
</h1>

1. KNN
	- Can solve classification and regression.
	- Steps :
		- Step 1 : Intialize K values.
			- In sklearn it is 'n_neighbors' parameter. 
		- Step 2 : Find K Nearest Neighbors for the test data.
		- Step 3 : In K neighbors maximum number of category is our results.
	- Distance Metrics 
		- In sklearn it is 'p' parameter.
		1. Eucliedian Distance.
			- Measure over hypotenous.
		$$Distance = \sqrt{(x_{2} - x_{1})^2 - (y_{2} - y_{1})^2}$$
		2. Manhattan Distance.
			- Measured over sides.
		$$Distance = (x_{2} - x_{1}) - (y_{2} - y_{1})$$
	- For regression we will take the average distance of the nearest neighbors.
	- To Find the k neighbors we need check all the distance which in term comsume more time O(n).
	- 2 Technique to reduce the time complexity.
		- In sklearn it is 'algorithm' parameter.
		- These Technique will use binary tree which reduce the search interval by half at each level.
		1. KD Tree.
			- Uses Backtracing to get K neighbors for any new data point.
			- We take median to split the tree.
		2. Ball Tree.
			- Better than KD Tree.
			- Here, we group nearest neighbors until we get a single group.

---

2. Implementation of KNN.
	1. Import dataset.
	2. Segregate the independent and dependent variable.
	3. Train test Split.
	4. Model Training.
		- ```from sklearn.neighbors import KNeighborsClassifier```
		- ```from sklearn.neighbors import KNeighborsRegressor```
	5. Performance metrics.

---

<h1 align="center">
  Dimensionality Reduction
</h1>
--- 

1. Curse of dimension.
	- If we add a dimension the accuracy of model increase but if any unwanted feature is added to the model it will try to learn from the new feature that results in decrease of the accuracy.
	- Model Performance Degradation.
	- Two Ways to remove Curse of Dimensionality.
		1. Feature Selection.
		2. Feature Extraction(Dimensionality Reduction).

---

2. Feature Selection.
	- Used to select the most important feature which helps in output predication.
	- We may have 2 condition 
		1. Positive correlation.
		2. Negative correlation.
	- To quantify we have formula
	$$Cov(x, y) = \frac{\sum_{i = 0}^n[(x - \bar{x})^2 - (y - \bar{y})^2]}{(N - 1)}$$
	- But the is not particular range for the output.
	- Pearson - value ranges between 0 to 1.
	$$\rho_{x,y} = \frac{cov(x,y)}{\sigma_{x} \times \sigma{y}}$$

---

3. Feature Extraction.
	- We are extracting new feature, from the exhisting feature.To reduce the dimension.
	- Approch 1 : Direct project of points to other axis to reduce dimension.
		- Disadvantage is that we lose more information of other feature.
	- So,we use PCA for dimensionality reduction.
	- In PCA our main goal is to find best principal component line which captures the more variance.
	- We use Eigen decomposition on variance matrix to find eigen values and eigen vector.
	- Highest eigen value is the first principal component line which has high variance.
	- Projection of a point P on unit vector U
		- $Proj_{p}U = \frac{P \times U}{|U|}$ 
	- Aim : To find the unit vector which captures the maximum variance.
	- Steps:
		- Step 1 : Standardize the data.
		- Step 2 : Covariance matrix of x and y.
		- Step 3 : Find the eigen values and eigen vectors.
			- $A \times v = \lambda \times v$ 
		- Step 4 : Use eigen value and find the best principal component line.
		- High value of $\lambda$ will be our principal component line 1 which denotes the capture of high variance.

---

4. Implementation of PCA with sklearn.
	- ```from sklearn.decomposition import PCA```
	- ```pca = PCA(n_components = int_value )```
	- ```x_train = pca.fit_transform(x_train)```
	- ```pca.components_``` - given eigen vector.
	- ```pca.explained_variance_ratio_``` - gives the ratio of variance captured by the unit vector.
	
---
