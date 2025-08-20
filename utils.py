import pygame, os 

BASE_IMG_PATH = "fotitos y audio/"

def load_image (path) :
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path) :
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path) :
        images.append (load_images + '/' + img_name)
    return images