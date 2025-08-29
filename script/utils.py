import os

import pygame

BASE_IMG_PATH = 'img/'

def load_image(path, scale=None):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    if scale :
        img = pygame.transform.scale(img, scale)
    return img

def load_images(path, scale=None):
    images = []
    full_path = os.path.join(BASE_IMG_PATH, path)

    for img_name in os.listdir(full_path):
        img_path = os.path.join(path, img_name)
        images.append(load_image(img_path, scale))

    return images