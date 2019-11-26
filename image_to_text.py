import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("temp1.png") # the second one 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
imr=Image.open('temp2.jpg')
text = pytesseract.image_to_string(imr)
print(text)
