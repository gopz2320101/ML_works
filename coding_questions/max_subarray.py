class solution:
    def max_sub_array(self, nums:list[int])->int:
        
        total_sum=max_sum=nums[0]
        
        for i in nums[1:]:
            total_sum=max(i,total_sum)
            max_sum=max(total_sum,max_sum)
            
        return max_sum


