<h1 align="center"  style="color: purple;">Natural Language Processing</h1>

- Object Detection we will given an image which contains multiple object to interest then we have to detect the object in the image then we also locate that object with a bounding box.Therefore, it is called as **object detection and localization**. 
- Object Detection will help also in the image classification.By detecting object and cropping object then send for classification which help in classification.
- Training data is prepared using the *annotation tools* like **Roboflow**

---

<h2 align="center" style="color: orange;">RCNN</h2>  

- RCNN = Recurrent Convolution Neural Network
- This is a naive approch to detect the object which is good for understanding object detection intially but we won't implement these as there is complexity in computation.
- Here, the input image is cropped (cropping is done in sliding window approch) and then sent to image classification.
- Problem:
    - We don't know where our image is present.
    - Selecting of sliding window size.
- In RCNN we have 2 aspects:
    1. Generationg of region proposals(images crop).
        - Sliding window.
        - **Selective search** - groping of pixels having same texture to generate segments.
    2. Which algorithm to apply for classification.
- In RCNN we follow the following steps,
    1. We take **a image** from the dataset.
    2. We crop that single image into **2000 crops** of different size.
    3. We **resize** the crops in order to convert all crops into same shape.
    4. The resized crops are passed into a **pretrained CNN**(can use Alexnet which is trained on our data) which can do classification.
    5. Pretrained CNN will generate **feature vector (4096)** for each crop i.e we get 2000 feature vector.
    6. Those feature vectors are passed into different **SVM**(which is trianed on our data) for detection of which object of interest is present in crop.
    7. Then we **backtrack** to our image to **label the crop**.
    8. We continue all 7 steps for remaining images.
- **Non-Max Supression** = If we have multiple crops detecting same object then we *retain the highest confidence* crop and eliminate the overlapping crops(partically detected objects) which are present under that highest confidence crop.
- **Intersection Over Union** = Used to define overlapping of 2 different crops.

<p align="center"><img src="img/image-0.png" width="980" height="480"></p>

---

<h2 align="center" style="color: orange;">Fast RCNN</h2>

- We noticed that RCNN is a complex architecture but takes 47 sec for a image to detect object.
- So, we use Fast RCNN to detect the object and also find the cooridinates of the object.
- **Sub Sampling Ratio** : The region proposal present in the original image is placed in correct position on feature map using sub sampling ratio.
- **Steps** :
    - Step 1 : 
        1. We will have a **big size image** as input like (640 x 960).
        2. We tell *Selective Search* algorithm to **detect the region proposal** on the original image.
            - We create region proposal with the hypothesis that individual region proposal would atmost contain 1 object. 
    - Step 2 :
        1. Then we will apply **VGG net** on the original image to get the feature map of small size(40 x 60 x 512).
        2. To **place the region proposal in correct possition** on the feature map we use **sub sampling ratio** of vgg net which is 16.
            - sub sampling ratio = $\frac{224}{14}$ = 16 because input layer shape of vgg net is (224 x 224) then output shape is (14 x 14).
        - Now we *cannot apply classification algorithm* because all region proposal **shape are different** so we cannot flatten it.
    - Step 3 : 
        1. We use **ROC pooling** to convert all region proposal to **uniform shape**.
            - We divide the region proposal into (7 x 7) grid.
            - Then we apply the max pooling on each grid.
            - At the end, all our region proposal will be converted to same shape.
        - Now we *can apply the classification algorithm* to detect the object of interest.
    - Step 4 :
        1. We will take all the region proposal of shape (7 x 7 x 512) and **Flatten** it.
        2. We will apply **Fully Connected Dense Layer** of (4096) neuron.
        3. We will apply **Fully Connected Dense Layer** of (4096) neuron.
            - Now, split the into 2 path one layer will be the output of classification problem another will be the bounding box regressor.   
        4. We will apply **Dense layer** with (number of output class) neuron as it acts as output layer.
        5. In parallel to 4 we will apply **Bouding Box Regressor**.
            - Bounding Box Regressor will help to find the *height and width* of region of proposal and also *coordinate of center* of the region proposal . 
- Figure present in Faster RCNN.

---


