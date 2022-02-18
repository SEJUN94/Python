import cv2

img = cv2.imread("images/1.jpg",1) # 이미지 불러오기

cropped_img=img[100:500, 150:300]
dst = cv2.cvtColor(cropped_img, cv2.COLOR_BAYER_BG2GRAY)

(h,w) = dst.shape[:2]
(cX,cY) = (w/2,h/2)

rot_info = cv2.getRotationMatrix2D((cX,cY), 23, 1)
img_23 = cv2.warpAffine(dst, rot_info, (w,h))

cv2.imshow('test.image',cropped_img)
cv2.imwrite('images/iu2.jpg',cropped_img)
cv2.waitKey(0)

cv2.destroyAllWindows() # 모든 윈도우 창을 제거


