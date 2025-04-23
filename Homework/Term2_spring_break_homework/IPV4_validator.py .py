txt =input("Do it in the format ___.___.___.___:")
x = txt.split(".")

a = x.pop(0)
b = x.pop(0)
c = x.pop(0)
d = x.pop(0)

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if 0<=a<256 :
    e = 1
else:
    e = 0 

if 0<=b<256 :
    f = 1
else:
    f = 0 

if 0<=c<256 :
    g = 1
else:
    g = 0 

if 0<=d<256 :
    h = 1
else:
    h = 0 

if e+f+g+h == 4:
    print("Valid IP address")
else:
    print("Invalid IP address")