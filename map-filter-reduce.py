from functools import reduce

nums=[1,2,3,4]
print(list(map(lambda x:x*2,nums)))

nums=[1,2,3,4]
print(list(filter(lambda x:x%2==0,nums)))

nums=[1,2,3,4]
print(reduce(lambda a,b:a+b,nums))

nums=[5,6,7]
print(list(map(lambda x:x+1,nums)))

nums=[10,15,20]
print(list(filter(lambda x:x>12,nums)))