import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,"SUN",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"mercury",(110,180),cv2.FONT_HERSHEY_COMPLEX,0.34,(0,0,255))
cv2.putText(img,"venus",(190,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"earth",(300,270),cv2.FONT_HERSHEY_COMPLEX,0.52,(0,0,255))
cv2.putText(img,"mars",(400,270),cv2.FONT_HERSHEY_COMPLEX,0.489,(0,0,255))
cv2.putText(img,"Jupiter",(500,90),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
cv2.putText(img,"Saturn",(720,110),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255))
cv2.putText(img,"uranus",(950,130),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255))
cv2.putText(img,"neptune",(1080,130),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255))


cv2.imshow("ss",img)

cv2.imwrite("solar-system with name.jpg",img)

cv2.waitKey(0)