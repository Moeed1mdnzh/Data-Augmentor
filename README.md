# What-it-is
Data augmentation is a common method used in many deep and machine learning models.
## Why-it-is-important
in order to regularize the weights and prevent overfitting we are fortunately capable of using this procedure.
# Examples 
As you may have already seen in the description, This project is able to create over 100 images for only a single image.
#### Image-Processing-Methods
***1 - Changing Channels*** <br />
***2 - Transforming*** <br />
***3 - Changing The Lighting*** <br />
***4 - Random Circle And Rectangles*** <br />
***5 - Blurring*** <br />
***6 - Erosion*** <br />
***7 - Dilation*** <br />
***8 - Adding Noise*** <br />
***9 - Colorizing*** <br />
***10 - Adding Contours*** <br />
##### Couple-Of-Examples
![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/0%2C0.jpg)
|Channel Change|Transform|Lighting|Random Shapes|Blur|Erode|Dilate|Noise|Colorize |Contour|  
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C2.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C5.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C21.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C14.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C23.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C17.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C18.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C16.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C11.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C4.jpg)|
|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C1.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C8.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C22.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C15.jpg)| | | | |![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C13.jpg)|![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C3.jpg)|
| |![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C19.jpg)| | | | | | |![](https://github.com/Moeed1mdnzh/Data-Augmentor/blob/main/few_examples/%5B0%2C%201%5D%2C12.jpg)| |

*Empty cells are meant to say that more generated images from the particular column topic are available in the project*

# Steps

## Preprocessing
Open up a folder in terminal and enter the following command `git clone https://github.com/Moeed1mdnzh/Data-Augmentor.git` or simply download it on your own. <br /> <br />
install the required packages
```python
pip install -r requirements.txt 
``` 

In your main file create 2 variables with names `X, y`.
## Parameters
The object of the data augmentor takes 6 parameters in order to fine tune the augmentors. <br />
**1 - channel : Channel of the images in your dataset, Must be wether 3 or 1** <br />
**2 - scale : Defines the dimensions of the zooming box, The higher you set it, The less zoom you would get. 0.5 is set as default** <br />
**3 - shapes : Shapes that are supposed to be drawn on your images, Must be wether rectangle or circle or both, Both is set as default** <br />
**4 - rate : The amount of lighting in your images, 0.7 is set as default** <br />
**5 - stepSize : The step size of the zooming box, 10 is set as default** <br />
**6 - limit : The amount of shifting in your images, 0.3 is set as default**










