'''
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
Accepted
'''

class Solution:
    cache = { 0: 0,
              1: 1,
              2: 1 }
    
    def tribonacci_rec(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self.cache:
            return self.cache[n]

        else:
            self.cache[n] = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)   
            return self.cache[n]
        
    def tribonacci(self, n):
        if n <= 2:
            return 1 if n else 0
        _sum = 0
        first, second, third = 0, 1, 1
        for _ in range(3, n + 1):
            _sum = first + second + third
            first, second, third = second, third, _sum
        return _sum

def test():
    assert Solution().tribonacci(4) == 4, "Should be 4"
    assert Solution().tribonacci(5) == 7, "Should be 7"
    assert Solution().tribonacci(25) == 1389537, "Should be 1389537"
    assert Solution().tribonacci_rec(4) == 4, "Should be 4"
    assert Solution().tribonacci_rec(5) == 7, "Should be 7"
    assert Solution().tribonacci_rec(25) == 1389537, "Should be 1389537"
    
n = 25  
print(Solution().tribonacci(n))
test()

