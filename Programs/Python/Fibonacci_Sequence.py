# Numeros da Sequência de Fibonacci
# Fórmula matemátida F{n}=F{n-1}+F{n-2}

# Menu inical 
# 1 - repeat until n
# 2 - repeat x times
# 3 - repeat infinitely

x=int(input(" 1 - repeat until n. 2 - repeat x times. 3 - repeat infinitely. choose a numbero:".replace(".", "\n")))
a= 0
b= 1
c=0
print("/\  "*10)
print("  \/"*10)

# 1 - repeat until n
if x == 1:
  n=int(input("enter the maximum value of the fibonacci sequence:"))
  print("/\  "*10)
  print("  \/"*10)
  print(a)
  print(b)
  while(1):
    c = a + b
    if c > n:
      break
    a = b
    b = c
    print (c) 
    
# 2 - repeat x times
elif x == 2:
  n=int(input("Enter the number of fibonacci sequence numbers you want:"))
  i=3
  print("/\  "*10)
  print("  \/"*10)
  print("1 -",a)
  print("2 -",b)
  for l in range(n-2):
    c = a + b
    a = b
    b = c
    print (i, "-", c)
    i=i+1
    
# 3 - repeat infinitely
elif x == 3:
    print("/\  "*10)
    print("  \/"*10)
    print (a)
    print(b)
    for l in range(n):
     c = a + b
     a = b
     b = c
     print (c)
     n=n+1
