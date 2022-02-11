# 배수의 합

a = input("첫 수를 적으세요 : ")

b = input("끝 수를 적으세요 : ")

c = input("배수를 넣으세요 : ")

arr = range(int(a),int(b)+1)
sum = 0

for i in arr:
    d = i%int(c)
    if d == 0  :
        sum += i
        


print(f"배수의 합은{sum}입니다.")
print(f"{a}에서 {b}까지 {c}배수의 합은{sum}입니다.")
print("{}에서 {}까지 {}배수의 합은{}입니다.".format(a,b,c,sum))
print(a,"에서",b,"까지","배수의 합은",sum,"입니다.")