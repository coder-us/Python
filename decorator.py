def greet(fx):
    def mfx():
        print("Good Morning ")
        fx()
        print("Thanks for using this function ")
    return mfx
    
@greet
def hello():
  print("Hello chutiye world")

def add(a,b):
   print(a+b)

hello()

