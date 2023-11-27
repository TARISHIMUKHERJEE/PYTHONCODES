a=5
def GlobalValueChange():
    global a
    a=10
print("before call a=",a)#5
GlobalValueChange()#10
print("after call a=",a)
