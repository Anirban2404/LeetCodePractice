#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:32:25 2019

@author: anirban-mac
"""

"""
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both 
arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such 
that you cannot load all elements into the memory at once?
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            return self.set_intersection(nums1, nums2)
        else:
            return self.set_intersection(nums2, nums1)
        
    def set_intersection(self, nums1, nums2):
        # TWO POINTERS
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []
        #print(nums1,nums2)
        while pt1 < len(nums1) and pt2 < len(nums2):
            if pt1 == len(nums1):
                return res
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                res.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
            #print(res)
            #print(pt1,pt2)
        return res
    
    def intersect1(self, nums1, nums2):
        #HASHMAP
        num1dict = {}
        res = []
        
        for num1 in nums1:
            if num1 in num1dict:
                num1dict[num1] += 1
            else:
                num1dict[num1] = 1
        print(num1dict)
        
        for num2 in nums2:
            #res.append(num2)
            if num2 in num1dict:
                if num1dict[num2] == 1:
                    del num1dict[num2]
                else :
                    num1dict[num2] -= 1
                res.append(num2)
        return res
     
nums1 = [4,7,9,7,6,7]
nums2 = [5,0,0,6,1,6,2,2,4]

#print(Solution().intersect(nums1, nums2))
print(Solution().intersect1(nums1, nums2))