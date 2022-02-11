import random
 # 홀 / 짝을 고르시오.
 
# a = input("홀 / 짝을 고르시오 : ")
#
#
# rnd =random.random()*100
#
# rnd1 = int(rnd)
#
# print(rnd1)
#
# re = ""
#
# b = int(rnd1)%2
#
# if b == 0:
#     re = "짝"
# elif b != 0: 
#     re = "홀"
#
# if a == re:
#     print("정답입니다.")
# elif a != re:
#     print("틀렸습니다.")
#

    
    
com = ""
mine = ""
result = ""

mine = input("홀/짝을 넣으세요")
ran = random.random()
if ran > 0.5 :
    com = "홀"
else:
    com = "짝"

if com == mine:
    result = "이김"
else:
    result = "짐"
    
print(mine) 
print(com) 
print(result) 