<h1 align="center">Implementation of ANN in Keras</h1>

- Keras API is a wrapper around the Tensorflow.

1. Import library .
    - ```import tensorflow as tf```

2. Import dataset.
    - Here, we will use MNIST(Modified National Institute of Standards and Technology) dataset.
    - ```mnist = tf.keras.datasets.mnist```

3. Train Test Split.
    - ```(x_train_full, y_train_full), (x_test, y_test) = mnist.load_data()```

4. Train Validation Split.
    - Scaling of input faster computation inside system.
    - ```x_vaild, x_train = x_train_full[:5000] / float(x_train_full.max()), x_train_full[5000:] / float(x_train_full.max())```
    - ```y_vaild, y_train = y_train_full[:5000], y_train_full[5000:]```
    - ```x_test = x_test / float(x_train_full.max())```

5. Visualizing training or input data.
    - ```plt.imshow(x_train[0], cmap = 'binary')```
    - ```sns.heatmap(x_train[0], annot = True, cmap = 'binary')```

6. Model Creation.
    - ```layers = [tf.keras.layers.Flatten(...), tf.keras.layers.Dense(...)]```
    - ```model = krs.models.Sequential(layers)```

7. Model Compilation.
    - ```model.compile(loss = 'sparse_categorical_entropy', optimizer = 'SGD',metrics = ['accuracy'])```

8. Model Training.
    - ```history = model.fit(x_train, y_train, epochs = 30, validation_data = (x_vaild, y_vaild), batch_size = 32)```

9. Visualizing the loss and accuracy.
    - ```pd.DataFrame(history.history).plot()```

10. Prediction.
    - ```y_prob = model.predict(x_test)```
    - ```y_pred = np.argmax(y_prob, axis = -1)```

---
