from PIL import Image
im = Image.open("images/egg.png")
im = im.rotate(90)
im.save("images/rotatedegg.png")