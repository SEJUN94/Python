import cv2
#from PIL import Image

# image = Image.open("images/iu.jpg")
#
# image.show()

#img = cv2.imread("images/iu.jpg",0) # 이미지 불러오기
img = cv2.imread("images/IU1.jpg",1) # 이미지 불러오기
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)
print(dst)

cv2.imshow("IU", dst) # 불러온 이미지를 " "라는 이름으로 창 표시.

cv2.waitKey(0) # 키보드 입력이 들어올 때까지 창을 유지
cv2.destroyAllWindows() # 모든 윈도우 창을 제거


