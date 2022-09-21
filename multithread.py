import threading 

n=100

def print_hello():
  for i in range(n):
    print("Hello")
  
def print_hi(): 
    for i in range(n): 
      print("Hi") 

t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  

t1.start()
t2.start()