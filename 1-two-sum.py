class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recs = {}
            
        for x in range(len(nums)):
            num = nums[x]
            if (target-num) in recs.keys():
                return [x,recs[target-num]]
            else:
                recs[num]=x
        return []
