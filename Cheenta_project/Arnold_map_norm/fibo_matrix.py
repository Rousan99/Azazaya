#Kazi Abu Rousan
#cheenta project

from PIL import Image
from numpy import *

input_img = array(Image.open("Austin.png"))
limit = input_img.shape[0]

x,y = meshgrid(range(N),range(N))
xmap = (2*x+y) % N
ymap = (x+y) % N

for i in range(2):
 output = Image.fromarray(input_img)
 output.save("Austin_output%d.png" % i)
 input_img = input_img[xmap,ymap]
