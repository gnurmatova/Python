from PIL import Image
im = Image.open("images/egg.png")
size = (30, 30)
im.thumbnail(size, Image.ANTIALIAS )
im.save("images/neweggthumb.png")