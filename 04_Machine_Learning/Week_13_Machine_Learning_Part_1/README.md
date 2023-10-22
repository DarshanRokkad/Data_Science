# Introduction To Machine learning  

1. AI vs ML vs DL vs DS.  
---
2. Types of machine learning.
    - Supervised ML.
    - Unsupervised ML.
    - Semisupervised ML.
    - Reinforcement learning.  
---
3. Train, Test and Validation.  
---
4. Bias , Variance , Overfitting and Underfitting.
    - Bais -> related to training data.
        - Accuracy is more then low bias.
        - Accuracy is less then high bias.
    - Variance -> related to testing data.
        - Accuracy is more then low variance.
        - Accuracy is less then high variance.
    - Overfitting -> Low Bias and High Variance.
    - Underfitting -> High Bias and High Variance.
    - Generalized model -> Low Bias and low Variance(we have to focus on this model).  
---
5. Handling of missing values.
    - There are 3 mechanism why missing value occur.
        1. Missing Completely At Random(MCAR).
        2. Missing At Random(MAR).
        3. Missing Not At Random(MNAR).
    - Handling of missing values.
        - Droping the row or column contain missing values.
           - ```df.dropna()``` -> rowise.
           - ```df.dropna(axis = 1)``` -> columnwise.
        - Useful functions.
           - ```df['feature'].isnull().sum()```
           - ```df['feature'].notna()``` -> gives the rows which are not null.
           - ```df['feature'].unique()``` - to check the possible values of categorical data.
        - Imputation of missing values.
            1. Mean value imputation -> for normally distributed data.
               - ```df['feature'].fillna(df['feature'].mean() ,inplace = True)```
            2. Median value imputation -> for other than normally distributed data.
               - ```df['feature'].fillna(df['feature'].median() ,inplace = True)```
            3. Mode value imputation -> for Categorical data.
               - ```df['feature'].fillna(df['feature'].mode() ,inplace = True) ``` 
---
6. Handling of imbalance dataset.
    - Ratio of data present in the classification dataset will differ between category.
    - ```df['feature'].value_counts()``` - gives number of values present in each category.
    - ```pd.concat([list of feature to be concatinated])``` - concatinates multiple dataframe.
    - How to handle imbalance dataset.
        - ```from sklearn.utils import resample```
        1. Upsampling.
            - Creates the dataframe that has the upsampled values.
            - ```df_minority_upsampled = resample(df_minority,replace=True,n_samples=len(df_majority),random_state=value)```
        2. Downsampling.
            - Creates the dataframe that has the downsampled values
            - ```df_minority_downsampled = resample(df_majority,n_samples=len(df_minority),random_state=value)```
            - Downsampling is not good because we will loose the data.  
---
7. Smote.
    - Synthetic minority oversampling technique
    - adding data points to minority dataset
    - from sklearn.datasets import make_classification
    - ```x,y = make_classification(n_samples = 1000,n_redundant = 0,n_features = 2, n_clusters_per_class = 1,weights = [0.9],random_state = 12)``` 
    - ```from imblearn.over_sampling import SMOTE```
    - ```oversampling = SMOTE()```
    - ```x , y = oversampling.fit_resample(df[['f1','f2']],df['target'])```  
---
8. Data interpolation.
    - estimating unknown values within a dataset based on the known values
    - Types 
        1. Linear interpolation
           - ```y_interp = np.interp(x_new,x,y)``` - interpolate the y value for new x value based on known x and y
        2. Cubic interpolation using scipy
           - ```from scipy.interpolate import interp1d```
           - ```fun = interp1d(x,y,kind='cubic')```
           - ```y_interp = fun(x_new)```
        3. Polynomial interpolation
           - ```poly_fun = np.polyfit(x,y,value)``` - value can be anything like 2,3
           - ```y_interp = np.polyval(poly_fun,x_new)```  
---                 
9. Percentiles Quartiles.
    $$\text{Percentile rank of x} = \frac{\text{Number of values below x}}{\text{n}} \times 100 $$ 
    $$\text{Value at percentile} = [\frac{Percentile}{100} \times (n + 1)] ^{th} \text{ Value}$$
    - where, Value tells the position of the percentile element in Dataset 
    - Quartile
        - Q1 = 25 percentile
        - Q2 = 50 percentile (median)
        - Q3 = 75 percentile  
---
10. 5 Number Summary and Box Plot.
    - 5 number summary 
        1. Minimum (excluding outliers)
        2. Q1 - First Quartile
        3. Q2 - Second Quartile (median)
        4. Q3 - Third Quartile
        5. Maximum (excluding outliers)
    - ```Minimum , Q1 , median , Q3 , Maximum = np.quantile(list,[0,0.25,0.5,0.75,1])``` - calculation of 5 number summary using python  
    - Fence for identifying outliers
        $$\text{Lower fence = Q1 - (1.5 x IQR)}$$
        $$\text{Upper fence = Q3 + (1.5 x IQR)}$$
        $$\text{IQR(Interquartile range) = Q3 - Q1}$$
    - Box plot -> ```sns.boxplot(x = list)```  
---
11. Feature Extraction
    - Taking out the most important feature from the dataset.
    1. Feature Scaling 
        1. Standardization
            $$\text{Z}_{score} = \frac{X - \mu}{\sigma}$$
        2. Normalization [Min Max Scaler]
            - Min Max Scaler 
            $$X_{scaled} = \frac{X_{i} - X_{min}}{X_{max} - X_{min}}$$
            - Mostly used in deep learning for image data
            - range of this features will be [0,1]
        3. Unit Vector
            - Magnitude of a vector 
            $$\text{Unit vector, } \hat{x} = \frac{\vec{x}}{|\vec{x}|}$$
    2. Feature Selection
        1. Filter Method
        2. Embedded Method
        3. Wrapper Method
    3. PCA(Principal Component Analysics)
        - Dimensional Reduction  
---
12. Feature Scaling
    1. Standardization
       - ```from sklearn.preprocessing import StandardScaler```
       - ```scaler = StandardScaler()```
       - ```scaler.fit_transform(df[['f1','f2']])```
    2. Normalization - MinMaxScaler
       - ```from sklearn.preprocessing import MinMaxScaler```
       - ```min_max = MinMaxScaler()```
       - ```min_max.fit_transform(df[['f1','f2']])```
    3. Unit Vector
       - ```from sklearn.preprocessing import normalize```
       - ```normalize(df[['f1','f2']])``` - used in creation of data frame
    - 2D list to be given  
    - ```scaler.transform([[values,values]])``` - for any new data
---
13. Data Encoding
    - Encoding Categorical features values into numerical values
    - There are 4 Types of Data Encoding
        1. Nominal or OneHotEncoder Encoding.
           - Converts Categorical value into corresponding binary vector.
           - ```from sklearn.preprocessing import OneHotEncoder```
           - ```encoder = OneHotEncoder()```
           - ```encoded_values = encoder.fit_transform(df[['feature']]).toarray()```
           - ```encoded_df = pd.DataFrame(encoded,columns = encoder.get_feature_names_out())```
        2. Label Encoding.
            - Converts Categorical value into unique numerical label for each category.
           - ```from sklearn.preprocessing import LabelEncoder```
           - ```encoder = LabelEncoder()```
           - ```encoded = encoder.fit_transform(df[['feature']])```
        3. Ordinal Encoding.
            - Converts Categorical value into numerical value which is assigned based on its position in the order.
            - For the categorical data that have ranking.
            - ```from sklearn.preprocessing import OrdinalEncoder```
            - ```encoder = OrdinalEncoder(categories=[[values in order of rank]])```
            - ```encoded = encoder.fit_transform(df[['feature']])```
        4. Target Guided Ordinal Encoding.
            - Converts Categorical value into numerical value based on their relationship with target variable.
            - For the categorical data which have large number of unique categories.
            - ```mean_feature = df.groupby('categorical feature')['target feature'].mean().to_dict()```
            - ```df['encoded'] = df['categorical feature'].map(mean_feature)```
       - ```encoder.transform([[data]])``` - for any new feature calculation  
---
14. Covariance and Correlation 
    1. Covariance - tells the realtionship between 2 variables but there is no specific range for the variance values.
       $$cov(x,y) = \sum_{i=1}^n \frac{(x_{i}- \bar{x})(y_{i}- \bar{y})}{(n-1)}$$
       - ```df.cov()``` 
    2. Pearson correlation coeffient - gives correlation value in the range of -1 to +1.
       $$r = \frac{cov(x,y)}{\sigma_{x} \times \sigma_{y}}$$
       - ```df.corr()```
    3. Spearman rank correlation - considers the rank of the feature present and gives the correlation value. 
       $$r_{s} = \frac{cov(R(x),R(y))}{\sigma_{R(x)} \times \sigma_{R(y)}}$$
       - ```df.corr(method = 'spearman')```  
---
