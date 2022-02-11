def addminmuldiv(a,b):
    return a+b,a-b,a*b,a/b

a,b,c,d = addminmuldiv(4,5)
print(a,b,c,d)


a = addminmuldiv(4,5)
print(a)
print(a[0])