  def findDuplicate(self, nums: List[int]) -> int:
        # X = set(nums)
        # for i in X:
        #     if nums.count(i) > 1:
        #         return i
        
        # for i in range(len(nums)):
        #     x = nums.pop(0)
        #     if x in nums:
        #         return x
        
        while nums[nums[0]] != nums[0]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]