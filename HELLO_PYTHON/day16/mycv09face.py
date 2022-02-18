import cv2
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

 
# 사용자 입력
img = cv2.imread("images/iu.jpg")

src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray,1.3,5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows() # 모든 윈도우 창을 제거


