<h1 align="center">Optimizers</h1>

- Used to minimize the cost function.
- goal of the algorithm is to iteratively move towards the minimum of the cost function by adjusting the model's parameters.
- Gradient descent is very complicated.
- Various problem are present in gradient descent.
    - Multiple local minima.
        - While reducing the loss our point may get stuck at local minima as slope /gradient at local minima's is 0. 
    - Gradient are not consistent.
    - Sparse feature 
        - Few neuron will get less opportunity to get updated there weights as less data flows through it.

- Optimizer helps our gradient to reach global minima.

---

- Cost function of linear regression
    - Weight updation rule.
    $$W_{i+1} = W_{i} - \alpha \times \frac{dl}{dw}$$
    - Where,
        - $W_{i+1}$ = New Weight
        - $W_{i}$ = Current Weight
        - $\alpha$ = Learning Rate(denotes the rate of convergence)
        - $\frac{dl}{dw}$ = rate of change of loss w.r.t weight(Gradient or Slope at a point)
    - Normal gradient descent will take a lot of time to reach global minima.
---

- **Types of Optimizers**:
1. Gradient Descent with Momentum.
2. Adagrad.
3. RMS prop.
4. Adam.

---

1. **Gradient Descent with Momentum**:
    - Momentum enhances the standard gradient descent by introducing the momentum term.
    - Momentum term is the exponential moving average used to accelerate the rate of convergence and navigate the noise area effectively.
    - Accumulator is used to accumulate the history.
        $$m_{t} = [\beta \times m_{t-1}] + [(1 - \beta) \times \nabla J(\theta_t)]$$
        - Where, 
            - $\beta$ = Momentum parameter, typically set between 0 and 1.Determines the contribution of the previous momentum in the current update.
            - $m_{t-1}$ = previous momemtum. 
            - $\nabla J(\theta_t)$ = gradient of the cost function with respect to the parameters($\frac{dl}{dw}$).
    - Updation rule for weight parameter.
        $$w_{i+1} = w_{i} - \alpha \times m_{i}$$
        - Where, 
            - $m_{i}$ = Acculumator for current weight.
    - Updation = history + current
    - Momentum solve the problem of local minima by accelerating the parameters.
    - Problem in Momentum :
        - As we move faster there is high chance of missing global minima as then decelarate and come back to global minima.

---

2. **Adagrad**(Adaptive gradient):
    - Solve the problem of momemtum which miss out the global minima while converging.
    - Accumulator 
    $$v_{t} = v_{t-1} + [\nabla J(\theta_t)]^{2}$$
    - Updation rule for weight parameter.
    $$w_{i+1} = w_{i} - \left(\frac{\alpha}{\sqrt{v_{i} + \epsilon}} \times \frac{dl}{dw}\right)$$
    - Where, $\epsilon$ is the smooting parameter used to avoid 0 in the denominator when $v_{t}$ is 0.
    - When parameters which has seen big updates there updation becomes slower.
    - Adagrad used to balance the learning. 
    - Problem:
        - When $v_{t}$ become too less then $\frac{\alpha}{\sqrt{v_{t} + \epsilon}}$ become too high then training will die.

---

3. **RMS prop**:
    - Accumulator
    $$m_{t} = [\beta \times m_{t-1}] + [(1 - \beta) \times \nabla J(\theta_t)^{2}]$$
    - Updation rule for weights parameter.
    $$w_{t+1} = w_{t} - \left(\frac{\alpha}{\sqrt{v_{t} + \epsilon}} \times \frac{dl}{dw}\right)$$

---

4. **Adam**.
    - This is the combination of Momentum and RMS prop.
    - Accumulator
        $$m_{t} = [\beta_{1} \times m_{t-1}] + [(1 - \beta_{1}) \times \nabla J(\theta_t)]$$
        $$v_{t} = [\beta_{2} \times v_{t-1}] + [(1 - \beta_{2}) \times \nabla J(\theta_t)^{2}]$$
        $$\hat{m_{t}} = \frac{m_{t}}{1 - \beta_{1}}$$
        $$\hat{v_{t}} = \frac{v_{t}}{1 - \beta_{2}}$$
    - Updation rule for weights parameter.
        $$w_{t+1} = w_{t} - \left(\frac{\alpha}{\sqrt{\hat{v_{t}} + \epsilon}} \times \hat{m_{t}}\right)$$

--- 
