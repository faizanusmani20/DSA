                                      # 1. Head Recursion (Print 1 to N)

def head(num):
  if num < 1:
    return

  head(num-1)
  print(num)
  
n=int(input("Enter the value of N: "))
head(n)


                                      # 2. Tail Recursion (Print 1 to N)

def tail(current,num):
  if current > num:
    return

  print(current)
  tail(current+1,num)

n=int(input("Enter the value of N: "))
tail(1,n)
