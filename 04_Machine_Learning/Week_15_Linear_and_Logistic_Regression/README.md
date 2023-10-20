# Linear and Logistic Regression    
  
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
          
3. Polynomial Regression
    - We use this when our data has non linear relationship.
    - We will find BEST FIT CURVE.
    - Equation for polynomial with n degree for 1 feature  
    $$h_{\theta}(x) = (\theta_{0} \times x^0) + (\theta_{1} \times x^1) + (\theta_{2} \times x^2) + .... + (\theta_{n} \times x^n)$$
    - If we increase the polynomial degree then model will be overfit for data.
    - Multiple polynomial regression equation
        - For polynomial degree 2 and 2 features  
        $$h_{\theta}(x) = \theta_{0} + (\theta_{1} \times x_{1}^1 + \theta_{2} \times x_{2}^1) + (\theta_{3} \times x_{1}^2 + \theta_{4} \times x_{2}^2)$$  
          
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
        - ```regressor.predict(x_train)``` - predicting values
    5. Test model.
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
          
7. Multiple Linear Regression with Python.
    - same steps as of linear regression  
      
8. Ridge Regression [L2 regularization].
    - Used for Reducing Overfitting(low bias and high variance).
    - Using Ridge regression we avoid cost function to become 0 indead avoiding overfitting.
    - Cost Function(which is never 0)
    $$J(\theta) = \frac{\sum_{i=1}^n [ y_{i} - h_{\theta}(x) ]^2}{n} + \left(\lambda_{1} \times \sum_{i=1}^n(slope)^2 \right)$$
    - Where,
        - $ \lambda $ is hyperparameter 
    - As $ \lambda $ increase 
        - global minima move upwards.
        - slope decreases. 
    - ```from sklearn.linear_model import Ridge```
    - ```from sklearn.linear_model import RidgeCV```  
          
9. Lasso Regression [L1 regularization].
    - Used to do Feature Selection(by removing less correlated feature).
    - Cost Function
    $$J(\theta) = \frac{\sum_{i=1}^n [ y_{i} - h_{\theta}(x) ]^2}{n} + \left(\lambda_{2} \times \sum_{i=1}^n|slope| \right)$$
    - In lasso regression cost function will be 0 at 1 point at that point less correlated feature become 0.
    - ```from sklearn.linear_model import Lasso``` 
    - ```from sklearn.linear_model import LassoCV``` 

10. Elastic Net Regression.
    - Combination of Ridge regression and Lasso regression.
    - Used to reduce Overfitting and also do Feature Selection.
    - Cost Function
    $$J(\theta) = \frac{\sum_{i=1}^n [ y_{i} - h_{\theta}(x) ]^2}{n} + \left(\lambda_{1} \times \sum_{i=1}^n(slope)^2 \right) + \left(\lambda_{2} \times \sum_{i=1}^n|slope| \right)$$
    - ```from sklearn.linear_model import ElasticNet``` 
    - ```from sklearn.linear_model import ElasticNetCV``` 

11. [Forest Fire End to End Project.](https://github.com/DarshanRokkad/forest_fire)
    - Data Cleaning and EDA using raw dataset.
    - Model training, Selecting best model and Picking model using cleaned dataset.
    - Deployment
        - We use AWS Elastic Beanstalk and AWS Code Pipeline.

12. Logistic Regression.
    - Logistic

