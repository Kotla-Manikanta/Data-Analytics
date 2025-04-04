import numpy as n
# arr = n.array([1,2,3])
# print(type(arr))

# print(n.zeros((2,3)))
# print(n.ones((3,2)))
# print(n.arange(0,10,2))
# print(n.linspace(0,1,5))
# print(n.random.rand(2,2))


a=n.array([[1,2],[3,4]])
b=n.array([[2,0],[1,3]])

print(n.dot(a,b)) #matrix multiplication
print(n.transpose(a)) #transpose
print(n.linalg.inv(a)) #invertible

arr=n.array([[10,20,30,40,50]])
print(arr[0,1])


