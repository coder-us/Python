a=str(input("What you want to do : "))
if(a=="coding"):
    print("Start coding")
elif(a=="decoding"):
    print("Start decoding")

if(a=="coding"):
    b=str(input("Enter your code :")) 
    if (len(b)>=3):
        b=b[1:]+b[0]
        print(b)
elif(a=="decoding"):
    c=str(input("Enter your decode :")) [::-1]
    print(c)
