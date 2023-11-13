<h1 align="center">Forward and Backward Propogation</h1>

- Here, We have **Multi Layer Perceptron** i.e We have multiple hidden layer between input and output.

- **Objective** : To reduce the loss to make prediction value closer to the actual value by changing the weights and bais.

- **Forward Propogation** : This occurs when a neural network is more likely to predict or output certain values over others due to the influence of external factors. It's like having a predisposition towards specific outcomes.

- **Backward Propogation** : This happens during the training of a neural network when adjustments are made to the weights of connections between neurons based on the error in predictions. It's like fine-tuning the network to improve its accuracy by correcting the influence of different inputs

- **Loss Function** 
    $$W_{t_{new}} = W_{t_{old}} - \alpha \times \frac{dL}{dW}$$
    - $\alpha$ = learning rate used to control the speed of convergence.

- **Algorithm** : 
    1. Step 1 : Intialize weights and bias randomly.
    2. Step 2 : Calculate loss.
    3. Step 3 : Calculate the derivative w.r.t to all the weights and bais to reduce loss.
    4. Step 4 : Continue step 3 and step 4 until points reaches the global minima in the gradient descent.

---
