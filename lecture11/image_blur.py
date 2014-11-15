from PIL import Image
from PIL import ImageFilter

im = Image.open("images/egg.png")
im = im.filter(ImageFilter.BLUR)
im.save("images/eggblur.png")