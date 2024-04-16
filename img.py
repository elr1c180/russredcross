import numpy as np 
import cv2
import random
import os

def generate(name, folder_name):
    directory = f'pictures/{folder_name}'
    imgs = os.listdir(directory)

    pic = directory + f'/{imgs[random.randint(0, len(imgs)-1)]}'
    img = cv2.imread(pic)

    font = cv2.FONT_HERSHEY_COMPLEX

    cv2.putText(img, name, (200,725), font, 5, color=(0,0,255), thickness=2)

    id = random.randint(111111,999999)
    
    img_path = f'pictures/{name}_{id}.png'
    cv2.imwrite(f'pictures/{name}_{id}.png', img)

    return img_path