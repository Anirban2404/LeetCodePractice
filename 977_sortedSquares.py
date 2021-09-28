"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in 
non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squaredArr = []
        for num in nums: 
            squaredArr.append(num * num)
        return sorted(squaredArr)
            
    def sortedSquares_2(self, nums):
        left = 0
        right = len(nums) - 1
        squaredArr = [0] * len(nums)

        for i in range(right,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                squaredArr[i] = nums[right] * nums[right]
                right -= 1
    
            else:
                squaredArr[i] = nums[left] * nums[left]
                left += 1
              
        return squaredArr

if __name__=="__main__":    
    nums = [-5,-4,-3,-2,-1,3,20]
    print(Solution().sortedSquares(nums))
    print(Solution().sortedSquares_2(nums))

