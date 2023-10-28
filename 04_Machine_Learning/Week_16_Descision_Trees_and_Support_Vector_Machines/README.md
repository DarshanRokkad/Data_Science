<h2 align="center">
  Decision Tree
</h2>  

1. Decision Tree Classifier.
    - Classificatin problem.
    - Output values will be Categorical.
    - After splitting the parent node we have Measure The Impurity
        1. Entropy 
            - Used for small dataset because we have log in formula is used to calculate the impurity.
            - Formula 
            $$H(S) = - (P_{+} \times log(P_{+})) - (P_{-} \times log(P_{-}))$$
            - Where, 
                - $P_{+}$ = Probabiliy of positive category
                - $P_{-}$ = Probabiliy of negative category
            - Value range between 0 to 1
        2. Gini Impurity 
            - Used for large dataset because simple mathematics is used to calculate the impurity.
            - Formula 
            $$G.I = 1 - \sum_{i=1}^n P^2 $$            
            - Where, 
                - $P$ = Probabiliy of category
            - Value range between 0 to 0.5
    - Information Gain
        - To select the particular feature as parent node for splitting.
        - Formula 
        $$Gain = H(S) - \sum_{v \in value} \frac{|S_{v}|}{|S|} \times H(S_{v}) $$
        - Where, 
            - $H(S)$ = Entropy of parent node
            - $H(S_{v})$ = Entropy of the child node
            - $S_{v}$ = Size of child node
            - $S$ = Size of parent node
        - We have to choose the node which has more information gain as parent node.
    - If we have Continuous input feature we will consider threshold. 

---

2. Post-Pruning and Pre-Pruning.
    - Used to reduce the Overfitting.
    1. Post-Pruning: 
        - Step 1 : Construct the entire tree till leaf node.
        - Step 2 : Pruning of Decision Tree.
        - Suitable for small dataset.
    2. Pre-Pruning: 
        - We use Hyperparameter Tuning.

---

3. Implementation of Decision Tree Classifier.
    1. Separate the independent and dependent feature.
    - ```x = df.iloc[:,:-1]``` = independent feature.
    - ```y = df.iloc[:,-1]``` = dependent feature.
    2. Train Test Split.
        - ```from sklearn.model_selection import train_test_split```
        - No need to do Standard Scaling.
    3. Model Building.
        - ```from sklearn.tree import DecisionTreeClassifier```
        - ```classifier = DecisionTreeClassifier()```
        - ```classifier.fit(x_train,y_train)```
        - ```tree.plot_tree(classifier,filled = True)```  to visualize the decision tree.
    4. Prediction.
        - ```y_pred = classifier.predict(x_test)```
    5. Accuracy.
        - ```from sklearn.metrics import accuracy_score, classification_report```
    - For Pre-Prunning we use GridSearchCV same as used in linear regreesion but parameters will change.

---

4. Decision Tree Regressor.
    - Regression Problem.
    - Output values will be Continuous.
    1. Variance.
        - It is also error.
        - Formula :
        $$\text{variance} = \frac{(y_{i} - \bar{y})^2}{n}$$
        - Where,
            - $\bar{y}$ - Mean of output.
    2. Variance Reduction.
        - Formula : 
        $$\text{variance reduction} = variance(root) - \sum (W_{i} \times variance(child_i))$$
        - Where,
            - $W_{i}$ = size of child node / Size of parent node
    - we have to select the node which have more variance reduction.
    - Implementation is same as classifier only one change is 'criterion' parameter values.
        - ```from sklearn.tree import DecisionTreeRegressor```

---

<h2 align="center">
  Support Vector Machines
</h2>   

1. Support Vector Classifier.
    - Classification Problem
    - Here, We will have 1 best fit line and 2 marigin line.
    - Aim : To create best fit line and 2 marginal plane which passes the nearest point(support vector) to best fit line.
    - 2 Types of margin
        1. Hard margin - There will be no missclassified data points. 
        2. Soft margin - There will be missclassified or overlapping data points.
    - Formuls : 
        - ax + by + c = 0
        - y = $-(\frac{a}{b}) x - (\frac{c}{b})$
        - $w^T x + b = 0$
    - A vector will be perpendicular to the best fit line. 
    - if $\theta > 90^0$ then the distance will be positive.
    - if $\theta < 90^0$ then the distance will be negative.
    - Distance between the margin line = $\frac{2}{|w|}$
    - Now, our aim is to increase the distance between the margin lines.
    - Cost function for hard margin SVC 
        - $\text{Cost Function}_{hard margin} = Maximize_{w,b} \times \frac{2}{|w|}$
        - $\text{Cost Function}_{hard margin} = Minimize_{w,b} \times \frac{|w|}{2}$
    - Cost function for soft margin SVC
       $$\text{Cost Function}_{soft_margin} = Minimize_{w,b} \times \frac{|w|}{2} + \left(C_{i} \times \sum_{i=1}^n \eta_{i}\right)$$
        - Where,
            -  $C_{i} = \frac{1}{\lambda}$ = Hyperparameter
            -  $\eta_{i}$ = Summation of the distance of incorrect data points from the marginal plane.

---

2. Implementation of Support Machine classifier.
    - we can create the dataset.
        - ```from sklearn.datasets import make_classification```
        - ```x, y = make_classification(n_samples = 1000, n_features = 2, n_classes = 2, n_clusters_per_class = 2, n_redundant = 0)```
    1. Separate the independent and dependent feature.
    2. Train Test Split.
    3. Model Building.
        - ```from sklearn.svm import SVC```
        - ```classifier = SVC(kernel = 'linear')```
        - ```classifier.fit(x_train,y_train)```
    4. Prediction.
        - ```y_pred = classifier.predict(x_test)```
    5. Accuracy.
        - ```from sklearn.metrics import classification_report, accuracy_score, confusion_matrix```
        - ```confusion_matrix(y_test, y_pred)```
        - ```accuracy_score(y_test, y_pred)```
        - ```classification_report(y_test, y_pred)```
    - For Pre-Prunning we use GridSearchCV.

---

3. Support Vector Regressor. 
    - Constraint 
    $$|y_{i} - w^T \times x| <= \epsilon + \eta_{i}$$
    - Where,
        - $\epsilon$ = Marginal Error i.e distance between point to upper or lower most margin line.

--- 

4. Implementation of Support Machine Regressor.
    - we can create the dataset.
        - ```from sklearn.datasets import make_regression```
        - ```x, y = make_regression(n_samples = 1000, n_features = 2, n_targets = 1, noise = 3.0)```
    1. Separate the independent and dependent feature.
    2. Train Test Split.
    3. Model Building.
        - ```from sklearn.svm import SVR```
        - ```classifier = SVR(kernel = 'linear')```
        - ```classifier.fit(x_train,y_train)```
    4. Prediction.
        - ```y_pred = classifier.predict(x_test)```
    5. Accuracy.
        - ```from sklearn.metrics import r2_score```
        - ```r2_score(y_test,y_pred)```
    - For Pre-Prunning we use GridSearchCV on epsilon parameter also.

---

5. Support Vector Machine Kernels
    - Using kernels we will do tranformation on data for convertion lower dimension to higher dimension to easily sepearate points using linear SVC when there is more error or overlapping in data set.
    1. Polynomial kernel.
        - Formula 
        $$f(x,y) = (x^T \times y + c)^d$$
        - Where, 
            - $x^T \times y$ = [[$x_{1}^2$ , $x1 \times x2$][$x1 \times x2$ , $x_{2}^2$]]
            - $d$ = polynomial degree
        - Implementation
            - ```classifier = SVC(kernel = 'poly')```
    2. Radial Binary Function kernel.
        - Formula 
        $$K(x_{1},x_{2}) = exp\left(\frac{||x_{1} - x_{2}||^2}{2 \times \sigma^2}\right)$$
        - Implementation
            - ```classifier = SVC(kernel = 'rbf')```
    3. Sigmondal kernel.
        - Formula 
        $$S(x) = \frac{1}{1 + e^{-x}}$$
        - Implementation
            - ```classifier = SVC(kernel = 'sigmoid')```


---
