class Solution:
    def trap(self, height):
        """
        Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
        :type height: List[int]
        :rtype: int
        """
        water = 0
        for i in range(len(height)-1):
            max_left = 0
            max_right = 0
            j = i
            while j >= 0:
                max_left = max(max_left, height[j])
                j -= 1
            j = i
            while j < len(height):
                max_right = max(max_right, height[j])
                j += 1
            water += min(max_left, max_right) - height[i]
        return water
            
                
             

            
assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6