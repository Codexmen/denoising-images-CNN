import cv2
import numpy as np


def normalise(img):
    return img/255


def load_images(image_paths_array, size=(128,128)):
    images_list = []
    for path in image_paths_array:
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, size)
        images_list.append(normalise(img))
    return np.array(images_list)
