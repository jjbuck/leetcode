class Solution:
    def twoSum(self, nums, target):
        """
		Given an array of integers, return indices of the two numbers such tha
		they add up to a specific target. You may assume that each input would
		have exactly one solution, and you may not use the same element twice.
		
		Given nums = [2, 7, 11, 15], target = 9,

		Because nums[0] + nums[1] = 2 + 7 = 9,
		return [0, 1].
		
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = list(sorted(nums))
        inds = [i[0] for i in sorted(enumerate(nums), key=lambda x:x[1])]
        lo_index = 0
        hi_index = len(nums) - 1
        while lo_index < hi_index:
            pair_sum = sorted_nums[lo_index] + sorted_nums[hi_index]
            if pair_sum < target:
                lo_index += 1
            elif pair_sum > target:
                hi_index -= 1
            else:
                return inds[lo_index], inds[hi_index]