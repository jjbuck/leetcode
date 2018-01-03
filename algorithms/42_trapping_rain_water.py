class Solution:
    def trap(self, height):
        """
        Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
        :type height: List[int]
        :rtype: int
        """
        stack = []
        water = 0
        current = 0
        while current < len(height):
            while stack != [] and height[current] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if stack == []:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                water += distance*bounded_height
            stack.append(current)
            current += 1
        return water
                
            
                
             

            
assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6