import os
import pytesseract
import crayons
import glob

from PIL import Image, ImageEnhance

SCREENSHOT_DIR = "C:/Users/canno/OneDrive/Pictures/Screenshots"
IDENTIFIER = ""
thingy = True

def process_image(img):
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(3)

    sharper = ImageEnhance.Sharpness(img)
    img = sharper.enhance(1)

    brighter = ImageEnhance.Brightness(img)
    img = brighter.enhance(1)

    img = img.convert("L")
    #img = img.crop
    return img                 

while thingy:
    files = glob.glob(SCREENSHOT_DIR + "/Screenshot*.png")
    file_pic = os.path.join(SCREENSHOT_DIR, files[0])
    #screenshot = process_image(Image.open(file_pic))
    screenshot = Image.open(file_pic)
    screenshot.save(SCREENSHOT_DIR + '/scan.png')
    #os.remove(file_pic)
    result = pytesseract.image_to_string(screenshot)
    print(result)
    qna = result.split("\n\n")
    print(qna)
    for i in range(len(qna)):
        qna[i] = qna[i].replace('\n', ' ')
    print(qna)
    thingy = False
