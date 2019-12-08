from PIL import Image

img= Image.open('DSC07507.jpg')
r,g,b = img.split()
g.show()