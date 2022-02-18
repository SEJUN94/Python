import cv2
#from PIL import Image

# image = Image.open("images/iu.jpg")
#
# image.show()

img = cv2.imread("images/iu.jpg",1) # 이미지 불러오기
#img = cv2.imread("images/IU1.jpg",1) # 이미지 불러오기
(h,w)=img.shape[:2]
print(h,w)
#dst = cv2.resize(img, dsize=(int(w*3), int(h*3)), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(img, dsize=(0, 0), fx=5, fy=5, interpolation=cv2.INTER_LINEAR)




cv2.imshow("IU", dst2) # 불러온 이미지를 " "라는 이름으로 창 표시.

cv2.waitKey(0) # 키보드 입력이 들어올 때까지 창을 유지
cv2.destroyAllWindows() # 모든 윈도우 창을 제거


