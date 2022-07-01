import os
from os.path import isfile, join
import pytesseract
from googletrans import Translator
import re
import cv2

# here you gotta change the folder path
pathurl = "C:/Users/kvcae/Pictures/Screenshots"

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kvcae\AppData\Local\Programs\Tesseract-OCR\tesseract'
contenido = os.listdir(pathurl)
translator = Translator()
files = [join(pathurl, nombre) for nombre in contenido if isfile(join(pathurl, nombre))]

# here, you can choose all the pictures from a array
image = cv2.imread(files[3])

print('imagetamaño', image.shape)

#Here you can change the picture size
imagecortada = image[400: 600, 100:1300]

result = pytesseract.image_to_string(imagecortada)
result = re.sub("[}_]", "", result)
result = re.sub("\n\n", "", result)

print(result)

pepe = translator.translate(result, dest='es')
print(pepe.text)
cv2.imshow('imagencaptura', imagecortada)
cv2.waitKey(0)
cv2.destroyAllWindows()