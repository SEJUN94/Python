import cv2


img = cv2.imread("images/1.jpg",1) # 이미지 불러오기


cropped_img=img[130:300, 300:400]

cv2.imshow('test.image',cropped_img)
cv2.imwrite('images/iu2.jpg',cropped_img)
cv2.waitKey(0)

cv2.destroyAllWindows() # 모든 윈도우 창을 제거


