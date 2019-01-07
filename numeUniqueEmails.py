#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:25:47 2019

@author: anirban-mac
"""

"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com 
is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an 
email address, mail sent there will be forwarded to the same address without 
dots in the local name.  For example, "alice.z@leetcode.com" and 
"alicez@leetcode.com" forward to the same email address.  
(Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus 
sign will be ignored. This allows certain emails to be filtered, for example 
m.y+name@email.com will be forwarded to my@email.com.  
(Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  
How many different addresses actually receive mails? 
Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
"testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" 
actually receive mails
"""

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        uemails = set()
        for email in emails:
            #print(email)
            if "." in  email:
                email_part = email.split("@")
                if "+" in email:
                    email_part1 = email_part[0].split("+")
                    
                    #print (email_part1,email_part2)
                    email = email_part1[0].replace(".","") + "@" + email_part[1]
                else:
                    email = email_part[0].replace(".","") + "@" + email_part[1]
#            print(email)
            uemails.add(email)
        return(len(uemails))
            


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
"testemail+david@lee.tcode.com"]

print(Solution().numUniqueEmails(emails))