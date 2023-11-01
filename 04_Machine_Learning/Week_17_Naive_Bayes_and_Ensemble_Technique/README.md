<h2 align="center">
  Naive Bayes
</h2>  

1. Navie Bayes.
    - The Algorithm with use Baye's Theorem is called Naive Bayes
    - Independent and Dependent Events.
    - Formula for Probability of happening of event A and then happening of event B
    $$\text{P(A and B)} = P(A) \times P(\frac{B}{A})$$
    - Baye's Theorem
    $$P\left(\frac{A}{B}\right) = \frac{P(A) \times P(\frac{B}{A})}{P(B)}$$
    - Where,
        - $P\left(\frac{A}{B}\right)$ = Probability of event A given that event B has already been happened. 
        - $P(A)$ = Probability of event A.
    - Probability of event A given that multiple events has already been happened. 
    $$P\left(\frac{A}{(x_{1},x_{2},x_{3})}\right) = \frac{P(A) \times P(\frac{x_{1}}{A}) \times P(\frac{x_{2}}{A}) \times P(\frac{x_{3}}{A})}{P(x_{1} \times x_{2} \times x_{3})}$$

---

2. Variants of Naive Baye's 
    1. Bernoulli Naive Baye's.
        - Whenever our features are following bernoulli's distribution then we need to use Bernoulli Navie Baye's.
        - Used in NLP.
    2. Multinomial Naive Baye's 
        - We have to use this When our input is in the form of text.
        - Used in NLP.
    3. Gaussian Naive Baye's
        - We have to use this when our feature are following Gaussian distribution.

---

3. Implementation of Navie Baye's 
    - Implementation is same as of previous algorithm.
    - ```from sklearn.naive_bayes import GaussianNB```
    - ```gnb = GaussianNB()```

---

4. Deployment in Azure 
    - We have to use Web App service.
    - All configuration need for the project is done by Azure.
    - We can see the deployment status in Github Action part.

---

<h2 align="center">
  Ensemble Techniques - Bagging and Boosting
</h2>

1. Ensemble Technique 
    - Used to increase the accuracy and efficiency of the model.
    - Here we combine mutliple models and train them then we will do prediction.
    - Two Types of Ensemble Technique
        1. Bagging 
            - Random Forest Classifier or regressor
        2. Boosting 
            1. Ada Boost.
            2. Gradient Boost.
            3. XG Boost.
    - Bagging Ensemble Technique 
        - Random Forest.
        - The dataset is divided into multiple sample.
        - Basis learner are independent model which use some algorithm to predict.
        - We aggregate the result of all the model this aggregation is called BootStrap Aggregation.
        - The technique of combining models is called Custom Bagging.
        - We predict final output using Majority Voting Classifier for classification problem and calculating average for regression problem.  

---

2. Random Forest Classifier and Regressor.
    - Sample data is given to models using row sampling and feature sampling.
    - Voting Classifier
        - We use voting classifier to get final result.
        - For classification = majority voting classifier based on basis learner output.
        - For regression = average of basis learner output.
    - Here, all the basis learners are Decision Trees.
    - We use this Random Forest instead of Decision Tree because to get generalize model instead of overfitted model.

---

3. Out Of Bag Score Decision Tree.
    - While Training model using Random forest using training data few records will not be selected those Data are called as Out of Bag Data.
    - Here, in random forest we have a parameter called ```oob_score = False``` if we make this parameter as ```True``` then Out of Bag data is used as Validation Data.
    - Validation data is used for Calculating accuracy and performance of model.

---

4. Implementation using pipeline and Hyper parameter.
    1. Load Dataset.
    2. Perform EDA.
    3. Segregate independent and dependent features.
    4. Train Test Split.
    5. Pipelining - To automate the feature engineering.
        - ```preprocessor.fit(x_train, y_train)```
        - Used to automate the task like feature engineering.
        - Create the 2 list of numerical feature names and categorical feautre names.
        - automating feature engineering.
        - ```from sklearn.impute import SimpleImputer``` = To handle missing values
        - ```from sklearn.preprocessing import OneHotEncoder``` = For encodig categorical data 
        - ```from sklearn.preprocessing import StandardScaler``` = For scaling numerical data
        1. Create Pipeline.
        - ```from sklearn.pipeline import Pipeline```
        - ```pipeline_name = Pipeline(steps = [(name,object)])``` = generaly 
        - ```num_pipeline = Pipeline(steps = [('imputer',SimpleImputer(strategy = 'median')), ('scaler',StandardScaler())])``` = numerical feature
        - ```cat_pipeline = Pipeline(steps = [('imputer',SimpleImputer(strategy = 'most_frequent')), ('onehotencoder',OneHotEncoder())])``` = categorical feature
        2. Combining Pipeline 
        - ```from sklearn.compose import ColumnTransformer```
        - ```processor = ColumnTransformer([(name, pipeline name, related feature name list)])``` = generaly 
        - ```preprocessor = ColumnTransformer([('numerical_pipeline',num_pipeline,numerical_cols),('categorical_pipeline',cat_pipeline,categorical_cols)])```
    6. Model Training and Accuracy using single function - it will train and give the accuracy of the model.
        - Select best model having high accuracy.
    7. Hyperparameter tuning using Randomized Search CV
    8. Train model with Best Parameters.
        - ```from sklearn.ensemble import RandomForestClassifier``` = Classification Problem 
        - ```from sklearn.ensemble import RandomForestRegressor``` = Regression Problem 
---

5. Boosting Ensemble Technique.
    - We can solve both regression and classification.
    - All basis learners Models are sequentially connected to get Strong Learner. 
    - Weak Learner is one who have not learnt properly from training dataset.
        - Weak learner are Underfitted by combining multiple weak learners we can make generalized model.
    1. Ada Boost.
        - We have Decision Tree Stump as a weak learner here.
            - Decision Tree Stump is a Decision Tree with depth 1.
        - Steps to solve Ada boost in maths:
            - Step 1 : We create Decision Tree Stump and Select Best One using impurity check.
            - Step 2 : Sum of the total errors by assigning Sample Weights and performance of stump.
                - Performance of Stump = $\frac{1}{2}\times log_{e}[\frac{\text{1 - Total error}}{\text{Total error}}]$ .
                - Performance of Stump is the $\alpha$ value i.e weight.
            - Step 3 : Update Weights for Correctly and Incorrectly classified points.
                - For correctly classified points we have to decrease the weight so that decrease the probability of selecting correctly classifier points.
                - $\text{Updated Weight} = \text{Weights} \times e^\text{- Performance of stump}$
                - For incorrectly classified points we have to increase the weight so that increase the probability of selecting incorrectly classifier points.
                - $\text{Updated Weight} = \text{Weights} \times e^\text{Performance of stump}$
            - Step 4 : Normalized Weights Computation and Bins assingment.
            - Step 5 : Select datapoints to send to next stump = by generating random number and create new records using bins.
            - Step 6 : Stump 2 repeat all steps.
            - Step 7 : Final Prediction.
                - $f = \alpha_{1}(M_{1}) + \alpha_{2}(M_{2}) + .... + \alpha_{n}(M_{n})$
                - $\alpha$ is the perfomance of the stump which is calculated in step 2.
                - Select the output which have high performace of say.
    2. Gradient Boosting Algorithm.
        - Steps to solve Gradient boosting in maths:
            - Step 1 : Create a Base model.
            - Step 2 : Compute residuals, Errors.
            - Step 3 : Construct Full Depth Decision Tree.
            - Step 4 : Prediction output modification.
            - Step 5 : Final Results
                - $F(x) = h_{0}(x) + \alpha_{1} \times h_{1}(x) + ... + \alpha_{n} \times h_{n}(x)$
                - $F(x) =  \sum_{i = 0}^n[\alpha_{i} \times h_{i}(x)]$
   3. XgBoost Algorithm.
        - Extreme Gradient Boosting.
        - Steps to solve XgBoost in maths:
            - Step 1 : Create a Base model.
            - Step 2 : Construct Full Depth Decision Tree.
                - $\text{Similarity Weight} = \frac{(\sum Residual)^2}{\sum(P(1 - P))}$
                - $\text{Gain} = \text{(left node + right node) - root node}$
            - Step 3 : Prediction output modification.
                - For any new data pass through base model - $log(odds) = log\left(\frac{P}{1-P}\right)$
                - For any new data to Decision Trees = $\sigma(log(odds) + \alpha \times \text{Similarity Weight})$
                - Where, 
                - $\sigma(x)$ = Activation Function.
                - $log(odds)$ = Base Model output.
                - $\alpha$ = Learning Rate.
                - Similarity Weight of new record.
            - Step 4 : Final Results
                - $F(x) = \sigma (\text{Base learner} + (\alpha_{1} \times DT_{1}) + ... + (\alpha_{n} \times DT_{n}))$

---

6. Implementation of Boosting Algorithms.
    - For Classification Problem.
        - ```from sklearn.ensemble import AdaBoostClassifier```
        - ```from sklearn.ensemble import GradientBoostingClassifier```
        - ```from xgboost import XGBClassifier```
    - For Regression Problem.
        - ```from sklearn.ensemble import AdaBoostRegressor```
        - ```from sklearn.ensemble import GradientBoostingRegressor```
        - ```from xgboost import XGBRegressor```

--- 
