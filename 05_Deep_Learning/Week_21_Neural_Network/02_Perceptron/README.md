<h1 align="center">Perceptron</h1>

1. Biological Neuron 
    - Biological Neuron is everywhere in our body which sense the environment and take input through some sensory organs.  

   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Blausen_0657_MultipolarNeuron.png/1920px-Blausen_0657_MultipolarNeuron.png" width="500" height="300">

    - Dendrites of neuron sense the environment and send information to brain.
    - Axon process the information to brain in form of eletrical impulse to brain.
    - Axon terminal send the information to another neuron as output of present neuron.
    - Note: 
        - Input is taken by Dendrites.
        - Computation is done by Cell body.
        - Transmission is done by Axon.
    - Neuron do 2 things 
        1. Take input from environment.
        2. Process information and send output to next neuron.

--- 

2. Artifical Neuron
    - Artifical Neuron is called as Perceptron.
    - Perceptron takes input from different source and then assigns some weight to those inputs then do weighted average or summation then pass into activation function then activation function check the input with the threshold if input is greater then threshold then output will be sent to next neuron.
          
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/60/ArtificialNeuronModel_english.png" width="500" height="300">
     
    - Summation = $w_{1} \times x_{1} + w_{2} \times x_{2} + ...... + w_{n} \times x_{n} + bias$
    - Perceptron aim is to bring the predicted value( $\hat{y}$ ) near to actual value( y ) by reducing loss function by changing the weights and bais.
    - Weight Update Rule for a neuron.
        $$W_{new} = W_{old} - \alpha \times \frac{dL}{dW}$$
    - Weight Update Rule When loss is Mean Squared Error.
        $$W_{new} = W_{old} + \alpha \times (actual - predicted) \times x_{i}$$
    - By changing weights perceptron try to bring predicted value closer to actual value.
    - Perceptron Can minic AND gate and OR gate.
        - It will assign the random weights to input intially.
        - Calculate the output for the random weights.
        - There may be some errors in finding output so we have to reduce error by changing the weights.
        - Change weights until perceptron mimic the gate.
    - Perceptron cannot mimic XOR gate because there is only 1 perceptron and a simple activation function.  

---
