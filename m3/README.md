# Module 3
## Task
Train and  apply at least two models presented in the Module to other datasets than those used in class. Describe your objective and data, show descriptive statistics and plots, divide in test, validation and test sets, train the models and show performance measures and your conclusions. 

## Results
1. Create [synthetic image data](../geomsha.ipynb).
2. Generate lots of images with [low resolution](./data.ipynb). On local computer: 100000 images in 60s.
3. Fit [logistic regression](./logistic.ipynb) to the image data. Result: Low test accuray of 0.57.
4. Fit [umap](./umap.ipynb) to the image data. Result: umap can't separate any clusters.
5. Fit [random forest](./forest.ipynb) to the image data. Result: High test accuracy of 0.97.
6. Fit [neural network](./neural.ipynb) to the image data. Result: Best test accuracy of 0.98.
7. Stress test of random forest model with other image settings
    - Prediction on [pure black and white](./forest_stress_bw.ipynb) images. Result: Still good test accuracy of 0.94.
    - Prediction with [fluctuating midpoint](./forest_stress_center.ipynb) of the shapes: Bad test accuracy of 0.58.
8. Stress test of neural network model with other image settings