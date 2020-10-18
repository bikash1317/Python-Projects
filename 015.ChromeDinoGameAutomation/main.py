# image = ImageGrab.grab() - grabs the colored image
# image = ImageGrab.grab().convert('L')  - grabs black and grey image

from os import lseek
import pyautogui
from PIL import Image, ImageGrab  # pillow
import time
from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)
    return 

def isCollide(data):
#For bird 
    for i in range(145,300):
        for j in range(310,420):
            if data[i, j] < 40 :
                hit("down")                  # < 100 as the image must be black and grey 
                return True

# For grass 
    for i in range(145,300):
        for j in range(430,470):
            if data[i, j] < 40 : 
                hit("up")  # < 100 as the image must be black and grey 
                return True
    return False



if __name__ == "__main__":
    print("Hey Dino game starts in 3 seconds ")
    time.sleep(3)
    hit("up")
    while(True):
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # print(asarray(image))
        isCollide(data)


        # #Draw the rectangle for cactus
        # for i in range(145,300):
        #     for j in range(450,470):
        #         data[i,j] = 0

        # #Draw the rectangle for bird
        # for i in range(145,300):
        #     for j in range(310,420):
        #         data[i,j] = 0

        # image.show()
