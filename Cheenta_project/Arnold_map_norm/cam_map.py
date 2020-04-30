#link: https://editor.p5js.org/K.A.Rousan/sketches/RwofTFiRx


from PIL import Image
from numpy import*
import cv2

N = 480
x,y = meshgrid(range(N),range(N))
xmap = (2*x+y) % N
ymap = (x+y) % N


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("Original",frame)
    key = cv2.waitKey(2)

    output = frame[xmap,ymap]
    cv2.imshow("Arnold's_map",output)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
