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



                                      # 3. Head Recursion (Print N to 1)

def head(current,num):
  if current > num:
    return

  head(current+1,num)
  print(current)

n=int(input("Enter the value of N: "))
head(1,n)




                                              # 4. Tail Recursion (Print N to 1)



def tail(num):
  if num < 1:
    return

  print(num)
  tail(num-1)

n=int(input("Enter the value of N: "))
tail(n)



