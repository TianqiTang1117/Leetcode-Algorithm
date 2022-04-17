class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def find(index):
            if index==len(nums):
                ans.append(pre[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue
                if not used[i]:
                    used[i]=True
                    pre.append(nums[i])
                    find(index+1)
                    pre.pop()
                    used[i]=False
        used=[False]*len(nums)
        ans=[]
        pre=[]
        find(0)
        return ans

        