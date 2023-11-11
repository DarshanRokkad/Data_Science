<h1 align="center">Activation Function</h1>

Types of Activation Function:
1. Sigmoid.
2. Softmax.
3. Tanh.
4. ReLU.
5. Parameteric ReLU.
6. Leaky ReLU.

---

1. Sigmod Activation Function.
    ![sigmod](https://miro.medium.com/v2/resize:fit:750/format:webp/0*GFQGn2yu4kghjW2W.jpg)
    - This function is also called as Squashing Function.
    - Used in Binary Classification Problem(used in logistic regression).
    - Used in perceptron output to squash the output value between 0 to 1.
    - Used to learn non-linearity present in the data in multilayer perceptron.
        $$\sigma(x) = \frac{1}{1+e^{-x}}$$
    - Graph vary between 0 to 1.
    - Derivative : $\sigma'(x) = \sigma(x) \times [1-\sigma(x)]$
        - Derivative max value is 0.25
        - As derivative is less it suffers a phenomenon vanishing gradient descent.

---

2. Softmax function.
    - Softmax is generalized form of sigmod activation function.
    - Used in Multiclass Classification Problem.
    - Used in perceptron output to squash the output value between 0 to 1.
    $$S(x) = \frac{e^{x_{j}}}{\sum_{i = 1}^{n}e^{x_{i}}}$$ 
    - Gives the probability of the particular class.

---

3. Tanh function.
    - Similar to Sigmoid.
    ![tanh](https://miro.medium.com/v2/resize:fit:750/format:webp/0*FIFkhXuir7JO0Utc.jpg)  
    - Value will range in between -1 to +1.
    - Used to Create a Neural Network for non-linear data.
    $$tanh = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$$
    - Graph is symmetric across 0.
    - Derivative : $tanh' = 1 - tanh^{2}$
        - Derivative max value is 1


---

4. ReLU.
    - Rectified Linear Unit.
    ![relu](https://vidyasheela.com/web-contents/img/post_img/40/ReLU-activation-function-new.png)
    - Used as an activation function in mutlilayer perceptron to bring in non-linearity in data.
    $$ReLU(x) = max(x, 0)$$
    - ReLU is more cruial to negative values.
    - If curve has 2 different slope at 2 different point then there will be non-linearity in the data.

---

5. Parameteric ReLU.
    - Parameteric Rectified Linear Unit.
    $$\text{ReLU = x , if x > 0}$$
    $$\text{ReLU = 0 , if x = 0}$$
    $$\text{ReLU} = \alpha \text{x , if x < 0}$$

---  

![parameteric and leacky ReLU](https://blogs.brain-mentors.com/content/images/2022/06/2813863991-5e720eab30026_articlex.png)

---  

6. Leaky ReLU.
    - Leaky Rectified Linear Unit.
    $$\text{ReLU = x , if x > 0}$$
    $$\text{ReLU = 0 , if x = 0}$$
    $$\text{ReLU = 0.01 x , if x < 0}$$
    - $\alpha$ value is fixed to 0.01 in Leacky ReLU.

---