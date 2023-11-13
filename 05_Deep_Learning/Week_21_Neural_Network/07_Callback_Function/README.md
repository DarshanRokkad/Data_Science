<h1 align="center">Callbacks</h1>

- Used to Managing our Neural Network.

- **Types** :
    1. Early Stopping Callback.
    2. Model Checkpoint Callback.
    3. Tensorboard Callback.

1. **Early Stopping Callback**:
    - Used to moniter the improvement of model and stop the training when the model doesn't improve behind a certian threshold.
    - Model will check after every iteration.
    - Used to save the computational power and cost effective.
    - We have 2 parameters here. 
        1. Patience.
            - Used to compare validation loss of current epoch with the (current - patience)epoch. 
        2. Minimum delta.
            - It is like a threshold used to stop training if difference between current epoch and (current-patience) epoch is less than min delta.
    - Implementation
        - We have to just add the callbacks while training our model.
        - ```es_cb = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', mode = 'min', patience = 5)```
        - ```history = model.fit(x_train, y_train, epoch = 5, batch_size = 32, validation_data = (x_valid, y_valid), callbacks = es_cb)```

2. **Model Checkpoint Callback**:
    - Used to save the weights and bais of the model where our model accuracy is max.
    - Basically save the checkpoint at best accuracy.
    - Implementation 
        - We have to just add the callbacks while training our model.
        - we need a file with extension '.h5' to save the best weights and bais.
        - ```mc_cb = tf.keras.callbacks.ModelCheckpoint(filepath = 'model_ckpt.h5', save_best_only = True)```
        - ```history = model.fit(x_train, y_train, epoch = 5, batch_size = 32, validation_data = (x_valid, y_valid), callbacks = mc_cb)```

3. **Tensorboard Callback**:
    - Used to log events on the tensorboard.
    - It is like a visualization tool.
    - Used to check how our model loss or accuracy is changes over the epoch.
    - Implementation
        - ```%load_ext tensorboard```
        - ```tb_cb = tf.keras.callbacks.TensorBoard(log_dir = 'logs', histogram_freq = 1)```
        - ```history = model.fit(x_train, y_train, epoch = 5, batch_size = 32, validation_data = (x_valid, y_valid), callbacks = tb_cb)```
        - ```%tensorboard --logdir="logs"``` = to open the tensor board dashboard.

- Combination of Early Stopping callback and Model Checkpoint callback make model training and monitering much more easier by stopping model training while loss increases and by saving the best model accuracy.
- We can use all the Callbacks in training the model.
    - ```history = model.fit(x_train, y_train, epoch = 5, batch_size = 32, validation_data = (x_valid, y_valid), callbacks = [es_cb, mc_cb, tb_cb])```

---    
