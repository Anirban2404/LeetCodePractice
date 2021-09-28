"""
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain 
an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
"""

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _countDigits = 0
        count = 0
        for num in nums:
            _countDigits = (self.countDigits(abs(num)))
            if self.checkEven(_countDigits):
                count += 1
        return count
    
    def countDigits(self, num):
        count = 0
        while num != 0 :
            num //= 10
            count += 1
        return count
    
    def checkEven(self, num):
        if num%2 == 0:
            return True
        else:
            return False
    
        
if __name__ == '__main__':
    nums = [555,901,482,1771]
    print(Solution().findNumbers(nums))