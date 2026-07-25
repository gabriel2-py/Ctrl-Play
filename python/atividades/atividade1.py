x = int(input(""))

if x==1:
    print("0")

elif x==2:
    print("0")
    print("1")

elif x>=3:
    print("0")
    print("1")
    print("1")

a = 1
at = 1
p = 0
if x > 3:
    for i in range(x-3):
        p = a + at
        print(p)
        a=at
        at=p