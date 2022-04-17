class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        ans={}
        m=50000
        for i in nums:
            if i not in ans.keys():
                ans[i]=0
            ans[i]+=1
        val=ans[max(ans,key=ans.get)]
        def check(key,nums):
            fir=nums.index(key) if key in nums else -1
            nums.reverse()
            last=nums.index(key) if key in nums else -1
            last=len(nums)-last
            return last-fir
        for key in ans.keys():
            if ans[key]==val:
                m=min(check(key,nums),m)
        return m



        