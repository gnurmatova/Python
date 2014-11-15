from PIL import Image
from PIL import ImageDraw

im = Image.open("images/mariostar.png")

draw = ImageDraw.Draw(im)
draw.line((0, im.height()/2)+(im.width(),im.height()/2), fill="red")
im.save("images/drawmario.png")