<h2 align="center">
  Linear Regression
</h2>  

---
1. Simple Linear Regression
    - Here, We have 1 independent feature and 1 dependent feature.
    - We will find a BEST FIT LINE.
        1. By reducing error.
        2. Error can be measured using cost function.
        3. We get gradient descest.
        4. By using Convergence algorithm we can try to minimize error until error reaches global minima. 
    - Line Equation   
        $$h_{\theta}(x) = \theta_{0} + \theta_{1} x$$
        - Where, 
            - $h_{\theta}(x)$ = predicted value. 
            - $\theta_{0}$ = intercept or coeffient.  
            - $\theta_{1}$ = slope of the line.
            - x = data points
    - Cost function[Mean Squared error]
        - Used to quantify how well a model's predictions align with the actual data.
        - Cost Function Equation  
        $$J(\theta_0 , \theta_1) = \frac{\sum_{i=1}^n [ y_{i} - h_{\theta}(x) ]^2}{n}$$
        - Where,
            - $y_{i}$ = actual value.
            - $h_{\theta}(x)$ = predicted value.
        - Gobal minima is the least possible value of cost function.
        - We get a Convex function - which has only 1 global minima.
        - Gradient descent 
            - optimizer algorithm used to max or min function.
            - Gradient descent in linear regression is a parabola.
            - It is obtained when plot $\theta$ v/s $J(\theta)$
    - Convergence algorithm
        - Used to determine when an iterative process, like an optimization algorithm has reached an optimal solution.  
        $$\theta_{j} = \theta_{j} - \alpha \times \left( \frac{\partial J(\theta_j)}{\partial \theta_j} \right)$$
        - Where,
            - $\theta_{j}$ = slope of the line.
            - $\alpha$ = learning rate (tells the speed of convergence).
            - $\frac{\partial J(\theta_j)}{\partial \theta_j}$ = derivate (tells the slope at specific point in cost function).  
---
2. Multiple Linear Regression
    - Here, we have more than 1 independent feature and 1 dependent feature.
    - We will find BEST FIT PLANE.
    - Gradient descent in linear regression is a 3D-parabola.
    - General equation from multiple linear regression 
    $$h_{\theta}(x) = \theta_{0} + \theta_{1} x_{1} + .... + \theta_{n} x_{n}$$ 
    - Where,
        - $h_{\theta}(x)$ = predited value.
        - $\theta_{0}$ = intercept or coefficient.
        - $\theta_{1}$ = slope of first feature.
        - $x_{1}$ = data points of first feature.
        - $\theta_{2}$ = slope of nth feature.  
        - $x_{n} $ = data points of nth feature.
---          
3. Polynomial Regression
    - We use this when our data has non linear relationship.
    - We will find BEST FIT CURVE.
    - Equation for polynomial with n degree for 1 feature  
    $$h_{\theta}(x) = (\theta_{0} \times x^0) + (\theta_{1} \times x^1) + (\theta_{2} \times x^2) + .... + (\theta_{n} \times x^n)$$
    - If we increase the polynomial degree then model will be overfit for data.
    - Multiple polynomial regression equation
        - For polynomial degree 2 and 2 features  
        $$h_{\theta}(x) = \theta_{0} + (\theta_{1} \times x_{1}^1 + \theta_{2} \times x_{2}^1) + (\theta_{3} \times x_{1}^2 + \theta_{4} \times x_{2}^2)$$  
---          
4. R Squared and Adjusted R Squared
    - Performance metrics.
    - Used to measure the accuracy of the model.
    1. R Squared  
        $$R_{squared} = 1 - \frac{{\sum{ (y_{i} - \hat{y_{i}})^2}}}{{\sum{ (y_{i} - \bar{y_{i}})^2}}}$$
        - Where,
            - $\sum{ (y_{i} - \hat{y_{i}})^2}$ = Sum of square residual (error occured with best fit line).
            - $\sum{ (y_{i} - \bar{y_{i}})^2}$ = Sum of square total (error occured with average $y_{i}$ line).
        - $R_{squared}$ value range between 0 to 1.
        - $R_{squared}$ value can be negative when best fit line is worse.
        - $R_{squared}$ value increase with addition of any type(strong or weak) new independent feature.
        - $R_{squared}$ = 1 then our model is overfitted.
    2. Adjusted R Squared
         $$Adjusted_{R_{squared}} = 1 - \frac{(1-R^2)\times(N-1)}{N-p-1}$$
        - Where,
            - $R^2$ = R square value.
            - N = Number of data points.
            - p = Number of independent feature.
        - Best unit for measure of accuracy
            - As $Adjusted_{R_{squared}}$ value increase with addition of new high correlated independent feature to model.
            - As $Adjusted_{R_{squared}}$ value decerase with addition of new less correlated independent feature to model.  
---              
5. Cost Functions
    - Used to quantify how well a model's predictions align with the actual data.
    - We consider cost function to reduce error .
    1. Mean Square Error(MSE):
        $$MSE = \frac{\sum_{i=1}^n(y_{i} - \hat{y_{i}})^2}{n}$$
        - Where,
            - $y_{i}$ = actual point
            - $\hat{y_{i}}$ = predicated point
            - n is total number of data points
        - Curve is parbola with one local minima and one global minima.
        - Curve is also called as CONVEX Function.
        - Advantage:
            1. Differentiable.
            2. It has one local minima and one global minima as curve is a convex function.
            - If a curve is a non-convex function then convergence will stop at local minima.
        - Disadvantage:
            1. Not robust to outliers.
            2. It is not in same unit as of input.
    2. Mean Absoulte Error(MAE):
        $$MAE = \frac{\sum_{i=1}^n|y_{i} - \hat{y_{i}}|}{n}$$
        - Advantage:
            1. It is robust to outliers.
            2. It is in same unit.
        - Disadvantage:
            1. Convergence takes time.
            2. Optimization become complex.
    3. Root Mean Square Error(RMSE):
        $$RMSE = \sqrt{\frac{\sum_{i=1}^n(y_{i} - \hat{y_{i}})^2}{n}}$$
        - Advantage:
            1. Differentiable - can find slope at any point on curve.
            2. It is in same unit.
        - Disadvantage:
            1. It is not robust to outliers.  
---              
6. Simple Linear Regression with Python.
    1. Divide the features based on independent and dependent features.
    2. Train, Test split of dataset.
        - ```from sklearn.preprocessing import train_test_split```
        - ```x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)```
    3. Standardize the data.
        - ```from sklearn.preprocessing import train_test_split```
        - ```x_train = scaler.fit_transform(x_train)```
        - ```x_test = scaler.transform(x_test)```
        - ```x_test = scaler.transform(x_test)```
    4. Train the model using LinearRegression
        - ```from sklearn.linear_model import LinearRegression```
        - ```regressor = LinearRegression()```
        - ```regressor.fit(x_train,y_train)```
        - ```regressor.coef_``` - coefficient or slope
        - ```regressor.intercept_``` - intercept
    5. Prediction.
        - ```y_pred = regressor.predict(x_test)``` - testing 
    6. Error calculation:
            - ```from sklearn.metrics import mean_squared_error,mean_absolute_error``` 
            - ```mse = mean_squared_error(y_test,y_pred)``` - mean square error 
            - ```mae = mean_absolute_error(y_test,y_pred)``` - mean absolute error
            - ```rmse = np.sqrt(mse)``` - root mean square error
    7. Accuracy calculation:
            - ```from sklearn.metrics import r2_score``` 
            - ```r_square = r2_score(y_test,y_pred)``` 
            - ```adjusted_r_square = 1 - ((1-r_square)*(n-1)/(n-p-1))``` 
    8.For any new data
        - ``` scaled_new_data = scaler.fit_transform(new_data)```
        - ``` pred = regressor.predict(scaled_new_data)```
    9. Assumptions.
        1. scatter plot actual value and predicted value if linear then model prediction is better. 
        2. distplot residuals if normal distribution then model prediction is better. 
        3. scatter plot residuals and predicted value if uniform distribution then model prediction is better.
    10. Pickling.
        - Used to serialising and de-serialising a python object structure.
        - When deploying we can use this pickle file for doing prediction on cloud.  
        - ```import pickle```
        - ```pickle.dump(regressor,open('model.pkl','wb'))``` - saving regressor into pickle file
        - ```model = pickle.load(open('model.pkl','rb'))``` - loading regressor to enviroment
        - ```model.predict(new_scaled_data)``` - predicting output
---          
7. Multiple Linear Regression with Python.
    - same steps as of linear regression  
---      
8. Ridge Regression [L2 regularization].
    - Used for Reducing Overfitting(low bias and high variance).
    - Using Ridge regression we avoid cost function to become 0 indead avoiding overfitting.
    - Cost Function(which is never 0)
    $$J(\theta) = \frac{\sum_{i=1}^n [ y_{i} - h_{\theta}(x) ]^2}{n} + \left(\lambda_{1} \times \sum_{i=1}^n(slope)^2 \right)$$
    - Where,
        - $\lambda$ is hyperparameter 
    - As $\lambda$ increase 
        - global minima move upwards.
        - slope decreases. 
    - ```from sklearn.linear_model import Ridge```
    - ```from sklearn.linear_model import RidgeCV```  
---          
9. Lasso Regression [L1 regularization].
    - Used to do Feature Selection(by removing less correlated feature).
    - Cost Function
    $$J(\theta) = \frac{\sum_{i=1}^n [ y_{i} - h_{\theta}(x) ]^2}{n} + \left(\lambda_{2} \times \sum_{i=1}^n|slope| \right)$$
    - In lasso regression cost function will be 0 at 1 point at that point less correlated feature become 0.
    - ```from sklearn.linear_model import Lasso``` 
    - ```from sklearn.linear_model import LassoCV``` 
---
10. Elastic Net Regression.
    - Combination of Ridge regression and Lasso regression.
    - Used to reduce Overfitting and also do Feature Selection.
    - Cost Function
    $$J(\theta) = \frac{\sum_{i=1}^n [ y_{i} - h_{\theta}(x) ]^2}{n} + \left(\lambda_{1} \times \sum_{i=1}^n(slope)^2 \right) + \left(\lambda_{2} \times \sum_{i=1}^n|slope| \right)$$
    - ```from sklearn.linear_model import ElasticNet``` 
    - ```from sklearn.linear_model import ElasticNetCV``` 
---
11. [Forest Fire End to End Project.](https://github.com/DarshanRokkad/forest_fire)
    - Data Cleaning and EDA using raw dataset.
    - Model training, Selecting best model and Picking model using cleaned dataset.
    - Deployment
        - We use AWS Elastic Beanstalk and AWS Code Pipeline.

---
<h2 align="center">
  Logistic Regression
</h2>   

---
1. Logistic Regression.
    - Used to solve classification problem.
        - Binary Classification - dependent feautre has 2 class.  
        - Multiclass Classification.  
    - Here, we use the Sigmoid Activation Function for Squashing the best fit line.Hence we can get output in the range 0 to 1. 
    - logistic regression Line equation
    - We don't use Cost Function of linear regression
        - When we plot a graph of $J(\theta)$ vs $\theta$ We get Non-Convex function where we have one global minima and many local minima.
        - At local minima's our slope will get 0.Hence, Our Convergence will get stuck at those local minima's.
        - So, in logistic Regression we use Log Loss Function
    - Cost Function - Log Loss Function  
        $$J(\theta_{0},\theta_{1}) = \left(-y_{i} \times log[h_{\theta}(x)] \right) - \left((1 - y_{i}) \times log[1 - h_{\theta}(x)] \right)$$
        - Where,
            - $J(\theta_{0},\theta_{1})$ = Cost Function.
            - $y_{i}$ = actual point.
            - $h_{\theta}(x)$ = predicted point.
---  
2. Logistic Regression with Regularization.
    1. L2 Regularization:
        - Used to Reduce overfitting.
        - Cost Function
        $$J(\theta_{0},\theta_{1}) = \left(-y_{i} \times log[h_{\theta}(x)] \right) - \left((1 - y_{i}) \times log[1 - h_{\theta}(x)] \right) + \left(\lambda_{1} \times \sum_{i=1}^n(slope)^2 \right)$$
    2. L1 Regularization:
        - Used to do Feature Selection.
        - Cost Function
        $$J(\theta_{0},\theta_{1}) = \left(-y_{i} \times log[h_{\theta}(x)] \right) - \left((1 - y_{i}) \times log[1 - h_{\theta}(x)] \right) + \left(\lambda_{2} \times \sum_{i=1}^n|slope| \right)$$
    3. Combination of L1 and L2 Regularization:
        - It is combination of L1 and L2 Regularization.
        - Cost Function
        $$J(\theta_{0},\theta_{1}) = \left(-y_{i} \times log[h_{\theta}(x)] \right) - \left((1 - y_{i}) \times log[1 - h_{\theta}(x)] \right) + \left(\lambda_{1} \times \sum_{i=1}^n(slope)^2 \right)+ \left(\lambda_{2} \times \sum_{i=1}^n|slope| \right)$$
    - In python it is denoted by -> penalty parameter.  
---      
3. Performance Metrics.
    1. Confusion matrix  
        |-|1|0|Actual value|
        |-|-|-|-|
        |1(Positive)|True Positive|False Positive||
        |0(Negative)|False Negative|True Negative||
        |Predicted value|-|-|-|
             
        $$\text{Accuracy of model} = \frac{TP + TN}{TP + FP + FN + TN}$$
    
    3. Accuracy 
         $$R^2 = 1 - \frac{{\sum{ (y_{i} - \hat{y_{i}})^2}}}{{\sum{ (y_{i} - \bar{y_{i}})^2}}}$$
        $$Adjusted_{R^2} = 1 - \frac{(1-R^2)\times(N-1)}{N-p-1}$$
        - For a Dumb model trained with imbalanced dataset our accuracy may be high so accuracy is not only measure. 

    4. Precision
        $$Precision = \frac{TP}{TP + FP}$$
        - We use this when False Positive(FP) is important.
        - Example : Spam classification [If mail is not spam but model predict that mail is spam]

    5. Recall
        $$Recall = \frac{TP}{TP + FN}$$
        - We use this when False Negative(FN) is important.
        - Example : Diabetes classification [If person has Diabetes but model tell he donot have Diabetes] 
    
    6. F-Beta Score
        $$F_{\beta} score = (1 + \beta^2) \times \frac{Precision \times Recall}{Precision + Recall}$$
        1. If FP is more important than FN.
            - $\beta$ = 0.5
        $$F_{0.5} score = (0.5) \times \frac{Precision \times Recall}{Precision + Recall}$$
        2. If both FP and FN are more important.
            - $\beta$ = 1
        $$F_{1} score = (2) \times \frac{Precision \times Recall}{Precision + Recall}$$
        3. If FN is more important than FP.
            - $\beta$ = 2
        $$F_{2} score = (5) \times \frac{Precision \times Recall}{Precision + Recall}$$

---
4. Cross Validation
    - Used internally in the Hyperparameter Tuning to select the best parameter.
    - We divide training data into 2 one for training and other for validation to make sure that correct hyperparameter is choosed.
    - We get different model accuracy for different values of randam_state so we use cross validation and calculate the average of all different accuracy.
    - Types  
        1. Leave One Out Cross Validation[LooCV]:
            - In entire training dataset we take only 1 datapoint for validation.
            - Disadvantage:
                - Training time increase 
                - Overfitting as we select the best hyperparameter.  
        2. Leave P out Cross Validation:
            - Here,it's is similar to LooCV but we take P datapoints out of training dataset for validation.  
        3. K-fold Cross Validation:
            - K denotes number of experiment to be done.
            - Validation datapoints are randomly selected.
            - we take average of accuracy of all the experiments.  
        4. Stratified K-fold Cross Validation:
            - Used in Imbalanced dataset.
            - It is same as K-fold CV but here we select the equal ratio for Validation.  
--- 
5. Hyperparameter Tuning
    - Used to select the best parameter for model training.
    - Types
        1. Grid Search Cross Validation:
            - Here, we do Grid Search + Cross validation
            - We try out all the combination and select the best accurate model then do Cross Validation.
            - Disadvantage:
                - Time for training increases.
        2. Randomized Search Cross Validation:
            - Here, We Have important parameter n_iter which tell take n random combination and do Cross Validation.
            - Advantage:
                - Time for training decreases.  
---
6. Logistic Regression with Hyperparameter Tuning With Python
    1. Divide the features based on independent and dependent features.
    2. Train, Test split of dataset.
        - ```from sklearn.preprocessing import train_test_split```
        - ```x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)```
    3. Hyperparameter Tuning.
        - To select the best parameters for our data.
        - Cross validation is done internally after selecting the best combination.
        - ```from sklearn.model_selection import GridSearchCV```
        - ```from sklearn.model_selection import RandamizedSearchCV```
        - ```cv_clf = GridSearchCV(classifier,param_grid = parameters,cv = 5)``` - parameters are one whose values to be choosed after hyperparameter tuning
        - ```cv_clf.fit(x_train,y_train)```
        - ```cv_clf.best_params_``` - best parameter that are selected from the given parameter after doing cross validation
        - ```cv_clf.best_score_``` - how much accuracy is given by best parameter
    4. Cross Validation.
        - Which is done internally in Hyperparameter Tuning.
        - ```from sklearn.model_selection import KFold```
        - ```cv = KFold(n_split = 5)```- n_split is the K value
        - ```from sklearn.model_selection import cross_val_score```
        - ```cv_scores = cross_val_score(classifier,x_train,y_train,scoring = 'accuracy',cv = cv)```
        - ```final_cv = np.mean(cv_scores)```
    5. Train the model using LogisticRegression with best parameters selected in Hyperparameter Tuning.
        - ```from sklearn.linear_model import LogisticRegression```
        - ```classifier = LogisticRegression(best parameters)```
        - ```classifier.fit(x_train,y_train)```
        - ```classifier.predict(x_train)``` - predicting values
    6. Prediction.
        - ```y_pred = classifier.predict(x_test)``` 
    7. Confusion Metrics, Accuracy and Classification Report:
            - ```from sklearn.metrics import confusion_matrix, accuracy_score, classification_report``` 
            - ```confusion_matrix(y_test,y_pred)``` 
            - ```accuracy_score(y_test,y_pred)``` 
            - ```classification_report(y_test,y_pred)``` 
    8. Pickling.
        - Same as Linear Regression. 
---
7. Logistic Regression Multiclass Classification
    - Two technique for mutliclass clasification
        1. One Versus Rest(OVR).
            - Uses OneHotEncoder encoding inside.
        2. Multinomial.  
---          
