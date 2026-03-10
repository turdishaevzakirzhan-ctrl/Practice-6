names=["a","b","c"]
for i,v in enumerate(names):
    print(i,v)

letters=["x","y","z"]
nums=[1,2,3]
for a,b in zip(letters,nums):
    print(a,b)

items=["p","q","r"]
for i,v in enumerate(items,1):
    print(i,v)

a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b)))

words=["hi","bye"]
nums=[10,20]
for w,n in zip(words,nums):
    print(w,n)