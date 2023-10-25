<h2 align="center">
  Decision Tree
</h2>  

---
1. Decision Tree Classifier.
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

2. Post-Pruning and Pre-Pruning.
    - Used to reduce the Overfitting.
    1. Post-Pruning: 
        - Step 1 : Construct the entire tree till leaf node.
        - Step 2 : Pruning of Decision Tree.
        - Suitable for small dataset.
    2. Pre-Pruning: 
        - We use Hyperparameter Tuning.

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

4. Decision Tree Regressor.
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

---
1. Support Vector Classifier.
    - 
    
