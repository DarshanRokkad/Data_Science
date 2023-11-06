<h1 align="center">
  Anamoly Detection
</h1>  

1. Anamoly Detection
    - Used to detect the outlier that we important for the our problem statement.
    - Types 
        1. Isolation Forest.
        2. DBSCAN - same DBSCAN clustering but the outlier points are the outliers.
        3. Local Outlier Factor Anamoly Detection.

---

2. Isolation Forest.
    - Internally Decision Tree is used.
    - We will find out the isolated point.
    $$S(x, m) = 2^{-\frac{E[h(x)]}{c(m)}}$$
    - Where, 
        - m = number of data points 
        - x = Data point
        - E[h(x)] = Average search depth for x form the isolated tree.
        - c(m) = Average value of h(x).
    - $S(x, m)$ = 1 then there is presence of outliers.
    - $S(x, m)$ = 0.5 it denotes there are only normal points.
    - Implementation
        - ```from sklearn.ensemble import IsolationForest```
        - ```clf = IsolationForest(contamination = 0.2)```
        - Visulaization of the outliers after fitting the data to the isolation forest
            - ```index = np.where(prediction < 0)``` = gets the index of the outliers
            - ```plt.scatter(x[index,0], x[index,1], edge_colors = 'red)``` - marking outliers data point color as red.

--- 

3. Local Outlier Factor Anamoly Detection.
    - Internally K-Nearest Neighbors is used.
    - It is a unsupervised learning outlier detection.
    - It compares local density of samples with local density of it's neighbors oto identify samples that have a lower density(outliers) than their neighbor.
    - if the average distance of a points is more then denstiy is less denotes that other points are far away = denotes that point is a outlier.
    - Implementation
        - ```from sklearn.neighbors import LocalOutlierFactor```
        - ```lof = LocalOutlierFactor(n_neighbors = 5)```
        - ```y_pred = lof.predict(x)```
        - Visualization of the outliers 
            - ```plt.scatter(x[:,0], x[:,1], c = y_pred)``` 

---

<h1 align="center">
  Time Series
</h1> 

1. Time Series.
    - There will atleast one feature that is related to timestamp.
    - Time stamp may be hourse, minute, seconds, day and month.
    - Two concepts to understand.
        1. Interpolation.
            - To Find out the value within the range.
            - Supervised ML.
            - The test data will comes in the range of training data.
            - Out of range values may lead to wrong prediction.
        2. Extrapolation.
            - To Find out the value outside the range.
            - The test data will not comes in the range of training data.
            - Here, We do forecasting and find the present value from the previous data.
    - There is time dependency in the time series data will depend on the previous dat.

---

2. Time Series Component.
    - 4 Types of Component.
        1. Trend 
            - Contains Upward, Horizontal and Downward trend.
        2. Season
            - It is the frequent repetation.
        3. Noise 
            - Some uncertinity in data because of unpredictable reason. 
        4. Cycle 
            - It is a cyclic pattern.
            - Cycle = Season + Noise.
    - 2 Types 
        - Multiplicative Time Series.
            - $Y_{t} = T \times S \times N$
            - Linear with time and have constant variable.
        - Additive Time Series.
            - $Y_{t} = T + S + N$
            - Non Linear with time and have non-constant variable.

---

3. Moving Average.
    - Used to Smoothing of Time Series to remove all the effect from the data.
    - moving means moving over time axis with some window size.
    - 3 Types of Moving Average.
        1. Simple Moving Average:
            - We fix the window size and then calculate the average.
            - Less window size then more specific to the point.
        2. Cumulative Moving Average:
            - Findout the average of all the upto the given time stamp.
            - Gives exponential trend.
        3. Exponential Moving Average:
            - Here, We give more weight to the recent datapoint or timestamp.
            - $V_{t} = (\beta \times V_{t-1}) + ((1 + \beta) \times \theta_{t})$
            - Where, 
            - $\beta$ is the amount of smoothing.
            - $V_{t}$ is the Value of current time stamp.

---

4. Stationary and Non-Stationary Time Series
    1. Stationary Time Series:
        - Mean and Variance will be constant.
    2. Non-Stationary Times Series:
        - Mean and Variance will be varing.
    - To Check Data is stationary or non-stationary time series.
        1. Visualization.
            - Histogram is used.
        2. Using Statistics.
            - ADF = Augmented Dickey Fullar Test is used.
    - To Convert non-stationary to stationary time series data.
        1. Differencing.
        2. Log.
        3. Root.
        4. Adjust of seasonal data.

---

5. ACF, PACF and Auto Regression.
    - Auto Correlation Function.
        - Auto = Correlation within same feature for particular time interval.
        - Correlation = given the amount of relationsship between 2 variable.
        - ACF measures the correlation between time series and it's lag value.
        - 1st lag value => D2 - D1 = $Y_{t-1}$
    - Partial Auto Correlation Function.
        - In PACF we remove the intermediate effect.
    - Auto Regression.
        - $Y_{t} = (\psi_{1} \times Y_{t-1}) + .... + (\psi_{n} \times Y_{t-n}) + C$
        - Where, 
        - $\psi$ is the coefficient term.

---

6. ARIMA
    - For model building in time series we use ARIMA.
    - Auto Regression Integrated Moving Average.
    - We use corrlogram for visualization.
    - Auto Regression(p)
        - $Y_{t} = (\psi_{1} \times Y_{t-1}) + .... + (\psi_{n} \times Y_{t-n}) + C$
        - We ACF to decide upto which term we have to consider.
    - Integration(d)
        - Differencing.
        - D1 = $Y_{t} - Y_{t-1}$
    - Moving Average(q)
        - Model building with error.
        - $Y_{t} = (\epsilon_{t-1} \times \psi_{t-1}) + .... + (\epsilon_{t-n} \times \psi_{t-n}) + C$
        - Where, $\epsilon$ is the error.
    - Combination of all 3 components is ARIMA.
    - Variants of ARIMA are SARIMA and SARIMX.

---


