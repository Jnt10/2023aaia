class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        N = len(nums) # 是你的nums的長度
        
        good = 0
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    good += 1
        return good