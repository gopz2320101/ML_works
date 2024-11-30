class solution:
    def shift_zero(self,num:list[int])->list[int]:
        prev=0
        for i in range(len(num)):
            if num[i]!=0:
               hide=num[prev]
               num[prev]=num[i]
               num[i]=hide
               prev+=1
        return num
    
lis=[0,10,0,11,12]

obj=solution()
lis=obj.shift_zero(lis)
print(lis)

print(lis[:])