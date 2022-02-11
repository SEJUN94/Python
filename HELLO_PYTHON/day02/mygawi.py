import random


user = input("가위/바위/보를 선택하시오 : ")
com = random.choice(["가위","바위","보"])
result = ""

print(com)

if com == user:
    result = "비겼습니다."
elif (com == "보" and user == "가위")or(com == "가위" and user == "바위")or(com == "바위" and user == "보"):
    result = "이겼습니다."
elif (com == "가위" and user == "보")or(com == "바위" and user == "가위")or(com == "보" and user == "바위"):
    result = "졌습니다."
    
print(result)
    