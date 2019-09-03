#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:59:42 2019

@author: anirban-mac
"""

"""
468. Validate IP Address

Write a function to check whether an input string is a valid IPv4 address or 
IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which 
consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 
172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, 
each group representing 16 bits. The groups are separated by colons (":"). 
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid 
one. Also, we could omit some leading zeros among four hexadecimal digits and 
some low-case characters in the address to upper-case ones, so 
2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading 
zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty 
group using two consecutive colons (::) to pursue simplicity. For example, 
2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the 
address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the 
input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""

class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        res = ""
        if "." in IP:
            res = self.searchIPV4(IP)
        elif ":" in IP:
            res = self.searchIPV6(IP)
        else:
            res = "Neither"
        return res
    
    # Check if the IP is IPv4
    def searchIPV4(self, IP):
        IPdomains = IP.split('.')
        #print(IPdomains)
        if len(IPdomains) != 4:
            return "Neither"
        for IPdomain in IPdomains:
            #print(IPdomain, len(IPdomain))
            if len(IPdomain) > 3 or len(IPdomain) == 0:
                return "Neither"
            if self.is_number(IPdomain):
                if int(IPdomain) > 255:
                    return "Neither"  
                continue
            else: 
                return "Neither"
        return "IPv4"
    
    # Check if the IP is IPv6
    def searchIPV6(self, IP):
        IPdomains = IP.split(':')
        #print(IPdomains)
        if len(IPdomains) != 8:
            return "Neither"
        for IPdomain in IPdomains:
            if len(IPdomain) > 4 or len(IPdomain) == 0:
                return "Neither"
            if self.is_hex(IPdomain):
                continue
            else: 
                return "Neither"
        return "IPv6"
    
    # Check if the domain is digital number
    def is_number(self, s):
        digits = set("0123456789")
        if len(s) > 1 and s[0] == '0':
            return False
        for char in s:
            if not (char in digits):
                return False
        return True
    
    # Check if the domain is hexadecimal number
    def is_hex(self, s):
        hex_digits = set("0123456789abcdefABCDEF")
        for char in s:
            if not (char in hex_digits):
                return False
        return True
        
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
IP = "1.0.1."
print(Solution().validIPAddress(IP))