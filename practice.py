# sentence=input("Enter the sentence :")
# vowel=consonent=0
# for i in sentence:
#     if i.isalpha():
#      if i in "AEIOUaeiou":
#         vowel+=1
#      else:
#         consonent+=1

# print("Consonent :",consonent)
# print("Vowel :",vowel)


def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
    
n=int(input("Enter the number :"))
if n<=0:
    print("Factorial does not exist")
else:
    print("Factorial of the number is ",fact(n))


    

    