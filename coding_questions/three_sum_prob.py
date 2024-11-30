#leet code problem 1.
class solution:
    def threesum(self,nums:list[int])->list[list[int]]:
        res=[]
        length=len(nums)
        nums.sort()
        
        for i in range(length-2):
            if i > 0 and nums[i]==nums[i+1]:
                continue
            l=i+1
            r=length-1
            
            while l<r:
                total=nums[i]+nums[r]+nums[l]
                
                if total<0:
                    l=l+1
                elif total>0:
                    r=r-1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    
                    while l<r and nums[l]==nums[l+1]:
                        l=l+1
                    while l<r and nums[r]==nums[r-1]:
                        r=r-1
                        
                    l=l+1
                    r=r-1
                    
        return res
    
           
a=[-4,-1,-1,0,1,2]                        
obj=solution()
res=obj.threesum(a)
print(res)