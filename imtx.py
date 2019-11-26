from pytesseract import image_to_string
from PIL import Image, ImageEnhance, ImageFilter


print (image_to_string(Image.open('temp1.png')))
print (image_to_string(Image.open('temp1.png'), lang='eng'))
