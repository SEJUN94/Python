import cv2
#from PIL import Image

# image = Image.open("images/iu.jpg")
#
# image.show()

img = cv2.imread("images/1.jpg",1) # 이미지 불러오기
#img = cv2.imread("images/IU1.jpg",1) # 이미지 불러오기
img180 = cv2.rotate(img, cv2.ROTATE_180)
height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 23, 0.30)
dst = cv2.warpAffine(img, matrix, (width, height))
print(img)
print(dst)
print(img180)

crop_img = img[60:410, 260:520]#슬라이싱
cv2.imshow("Cropped Image", crop_img)

#cv2.imshow("IU", dst) # 불러온 이미지를 " "라는 이름으로 창 표시.

cv2.waitKey(0) # 키보드 입력이 들어올 때까지 창을 유지
cv2.destroyAllWindows() # 모든 윈도우 창을 제거


