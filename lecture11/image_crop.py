from PIL import Image
im = Image.open("images/egg.png")
cropbox = 50, 50, 200, 200
im = im.crop(cropbox)
im.save("images/cropegg.png")