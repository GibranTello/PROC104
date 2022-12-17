import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("Output", img)

cv2.putText(img, "Sol", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Mercurio", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Venus", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Tierra", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Marte", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Jupiter", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Saturno", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Urano", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))
cv2.putText(img, "Neptuno", (100,800), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,225))