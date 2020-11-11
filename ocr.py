from PIL import Image
from mss import mss #old mss v2.0.22 required as of Nov2020
import pytesseract
import numpy as np
import cv2
import time



mon = {'top': 1250, 'left': 450, 'width': 1060, 'height': 70}
sct = mss()
counter = 0
cache = "so-far-empty-lol"

def text_rekognition(fname):
    outFile = open("myOutFile.txt", "a")
    textInside = pytesseract.image_to_string(fname)
    global cache

    if cache == textInside:
        outFile.close()
        return

    cache = textInside
    for symbol in textInside:
        if symbol != '\n':
            outFile.write(symbol)
        else:
            outFile.write('\n')
            break


while 1:
    if counter == 6:
        counter = 0
    pixels = sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    cv2.imshow('test', np.array(img))
    namePNG = "monitor%s.png" % counter
    sct.to_png(data=pixels, output=namePNG)
    counter += 1
    text_rekognition(namePNG)
    #if cv2.waitKey(25) & 0xFF == ord('q'):
    if cv2.waitKey(25)== ord('q'):
        cv2.destroyAllWindows()
        break
    time.sleep(1)




# outFile.write(pytesseract.image_to_string('1.png'))