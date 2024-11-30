import numpy as np

a=np.array([[1,2,3],[2,3,4],[3,4,5]])
b=np.array([[1,3,4],[3,3,6],[7,8,9]])

result1=np.dot(a,b)
print(result1)

result2=result1.transpose()
print(result2)

x=np.linspace(4,-4,9)

print(x)

y=np.meshgrid(x)
print(y)