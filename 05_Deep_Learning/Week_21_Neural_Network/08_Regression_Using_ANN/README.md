<h1 align="center">Regression Using ANN</h1>

- In Regression output will be a continuous value.

- If we have a dataset in the google drive we can mount that on the environment.
    - ```from google.colab import drive```
    - ```drive.mount('___')```

- Training is similary to the classification problem only change is the loss function.

1. Import the data.
2. Train Test Split.
3. Standard Scaling of input variable.
4. Model Creation.
5. Model Compilation.
    - ```model.compile(loss = 'mse', optimizer = 'SGD', metrics = ['accuracy'])``` # loss function will change
6. Model Training.
7. Model Prediction.

---
