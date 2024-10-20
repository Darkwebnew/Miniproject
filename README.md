# Heart Disease Segmentation Using MRI Images
Small Description about the integration of a deep learning-based segmentation model in MRI heart scans, aimed at enhancing diagnostic accuracy and providing medical professionals with an automated tool for identifying and segmenting heart structures.

## About
Heart Disease Segmentation Using MRI Images is a project designed to implement a deep learning model, specifically U-Net, to automatically segment key structures of the heart, such as the ventricles and myocardium, from MRI scans. Traditional segmentation methods are time-consuming and prone to human error. This project seeks to overcome these challenges by providing a tool that streamlines the process, ensuring faster and more accurate results for heart disease diagnosis.

## Features
Implements advanced U-Net architecture for heart segmentation.
A web-based interface for easy integration into clinical workflows.
High segmentation accuracy and efficiency.
Reduces manual intervention by automating the segmentation process.
Provides clear delineation of heart structures to aid in diagnosis.

## Requirements
Operating System: Compatible with 64-bit OS (Windows 10 or Ubuntu) for deep learning framework compatibility.
Development Environment: Python 3.6 or later is necessary for coding the MRI segmentation system.
Deep Learning Frameworks: TensorFlow for model training and heart segmentation tasks.
Image Processing Libraries: OpenCV for handling MRI images.
Version Control: Git for collaborative development and version tracking.
IDE: Use of VSCode or PyCharm for efficient coding and debugging.
Additional Dependencies: Includes scikit-learn, TensorFlow (versions 2.4.1), OpenCV, and Numpy for deep learning and image processing tasks.

## System Architecture
Input Layer: Preprocessed MRI heart images.
Model: U-Net convolutional neural network for pixel-wise segmentation.
Output Layer: Segmented MRI image with clear boundaries of heart structures such as the left ventricle, right ventricle, and myocardium.



## Output
Output 1: Segmented MRI image showing the delineated left and right ventricles. Screenshot of segmented heart regions

![image](https://github.com/user-attachments/assets/6201c6b2-a389-434d-80b7-45137573cd77)

Output 2: Visualization of myocardium in MRI scan. Screenshot of myocardial segmentation

![image](https://github.com/user-attachments/assets/bdc27cf8-aa90-434a-9af3-7c6b187fa5d4)

![image](https://github.com/user-attachments/assets/3c730e50-71fc-46ea-967a-38d36373153e)

![image](https://github.com/user-attachments/assets/0621e34a-4612-45b5-8ffa-fde9ffe7dc3a)

Detection Accuracy
Segmentation Accuracy: 94.8%
Note: These metrics are subject to further tuning based on validation datasets.

## Results and Impact
The Heart Disease Segmentation System significantly enhances the speed and accuracy of MRI heart scan analysis, offering a reliable tool for detecting and segmenting heart structures. This system aids radiologists and cardiologists in diagnosing heart conditions with greater precision, making healthcare more efficient.

The integration of deep learning in medical imaging showcases the potential for future improvements in automated diagnostic tools, contributing to the development of more advanced, inclusive healthcare technologies.

## Articles Published / References
