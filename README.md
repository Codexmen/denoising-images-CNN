## Motivation
Create a neural net to denoise images.

What is a noise image? -- this is an image that contain pixels with random color values.
Image can contain synthetic noise like Gaussian or natural due to low light of sceen during shooting.
Images could be grayscale or colored. 

This network trained to denoise color images with natural noise (like digital photos from smartphones)
## Introduction

You could see demo and comparing with Gaussian smoothing in file [compare](https://github.com/Codexmen/denoising-images-CNN/blob/main/compare.ipynb)
Training process and data preparation in file [SSID](https://github.com/Codexmen/denoising-images-CNN/blob/main/SIDD.ipynb)

Folders `model*` contain a few models that give pretty good results during experimentation. 
### Metrics 
If we have ground true images along with noised images there is a two metrics that we could use 
for measure performance:
- [PSNR](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio) - Peak Signal to Noise Ratio
- [SSIM](https://en.wikipedia.org/wiki/Structural_similarity) - Structural Similarity Index Measure

For both, the higher the score better it is.

### Datasets
Used datasets:
 - [SSID - Small Dataset](https://www.eecs.yorku.ca/~kamel/sidd/dataset.php) - contains 160 image pairs (noisy and ground-truth)
 - [PolyU-Real-World-Noisy-Images-Dataset-Public](https://github.com/csjunxu/PolyU-Real-World-Noisy-Images-Dataset) - provides the real-world noisy images
 
For checking results used [RENOIR](http://adrianbarburesearch.blogspot.com/p/renoir-dataset.html)   
## Description
For achieving good results with large images I split them to small chunks `64*64` pixels and use 
neural network architecture U-net with 4 layers of convolutions double each layer number of filters.
For training, we generated 50936 parts `64*64` and 12734 patches for validation.

# Demo
For demonstration, I use RENOIR dataset that was not used during training.

You could see demo and comparing with Gaussian smoothing in file [compare](https://github.com/Codexmen/denoising-images-CNN/blob/main/compare.ipynb)
Training process and data preparation in file [SSID](https://github.com/Codexmen/denoising-images-CNN/blob/main/SIDD.ipynb)
# Results
I compare results of predictions with Gaussian smoothing: 
#Conclusions

There is a more modern approaches to denoise images (a lot of them use implemented model as a baseline).
Next steps are use them:
- [KBNet](https://github.com/zhangyi-3/kbnet)
- [MIRNet](https://github.com/swz30/MIRNet)
- [MPRNet](https://github.com/swz30/MPRNet)
- PRIDNet
- etc.
