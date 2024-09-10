
def fib(k):
    if k <=1 :
          return k
    else:
          return fib(k-1) + fib(k-2)
    

def main():
        path = input("enter a number for fib sequence: \n")
        path = int(path)
        
        for i in range(path):
            print(fib(i))

main()  