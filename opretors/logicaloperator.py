# b=12
# x=5
# print(b>3 and b<10)
# print(b>3 or b<4)
# print(not(x>3 and x<10))/

username ="Ram"
password=123456

if(username=="Ram" and password==123456):
    print("login")
else:
    print("username or password not match")

if(username=="Ram" or password=='123456'):
    print("login")
else:
    print("username or password not match")

if(not(username=="Ram" or password=='123456')):
    print("login")
else:
    print("username or password not match")