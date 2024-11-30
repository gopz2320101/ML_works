a=int(input("enter the first number"))
b=int(input("enter the second number"))


print({a,b})
def swap(a,b):
  
  a,b=b,a
  return a,b

print("swapped",{swap(a,b)})