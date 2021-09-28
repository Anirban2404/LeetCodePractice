"""
1089. Duplicate Zeros
Given a fixed length array arr of integers, duplicate each occurrence 
of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return 
anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified 
to: [1,0,0,2,3,0,0,4]

Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified 
to: [1,2,3]
"""

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if len(arr) < 2:
            return arr
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr = self.shiftpos(arr, i)
                i += 1
            i += 1
        return arr
    
    def shiftpos(self, arr, pos):
        for i in range(len(arr) - 2, pos, -1):
            arr[i + 1] = arr[i]
        
        if pos == len(arr) - 1:
            return arr
        arr[pos + 1] = 0
        return arr
    
    def duplicateZeros2(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if len(arr) < 2:
            return arr
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr[i + 1] = arr[i]
            i += 1
            print(arr, '---> ', i)
        return arr
    
        
if __name__ == '__main__':
    arr = [1,0,2,3,0,4,5,0]
    #print(Solution().duplicateZeros(arr))
    print(Solution().duplicateZeros2(arr))