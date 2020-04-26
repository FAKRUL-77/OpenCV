import cv2

img = cv2.imread('images/fakrul.png', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/fakrul_copy.png', img)
    cv2.destroyAllWindows()

