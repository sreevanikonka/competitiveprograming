def couple(l):
   num=len(l)
   arr=[None]*num
   for i, p2 in enumerate(l):
       arr[p2]=i
   count=0
   for i in range(0,num,2):
       x, z=l[i:i+2]
       y=x-1 if x%2 else x+1
       if y!=z:
           j=arr[y]
           l[j]= z
           arr[z]=j
           count+=1
   return count 

print(couple([1,3,4,0,2,5]))
print("********************")


print(couple([3,2,0,1]))
print("********************")

print(couple([1,0]))
print("********************")
