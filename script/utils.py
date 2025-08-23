import pygame, os 

BASE_IMG_PATH = "img/"

def load_image (path) :
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path) :
    images = []
    for img_name in os.listdir("img/" + path) :
        images.append (load_images (path + '/' + img_name))
    return images