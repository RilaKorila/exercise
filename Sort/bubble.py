class Sort:
    def bubbleSort(self, nums: List[int]) -> None:
        
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                # if nums[j] is larger than nums[j+1], swap them
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]