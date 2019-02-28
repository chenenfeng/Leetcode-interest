"""
I made a mistake.
I want to delete the first and last element in the string,
1. I use strip: s1 = s1.strip(s1[0]+s1[1]), but it delete all the same element from start and end
failed
2. So I just make slice... I want to avoid.. s1 = s1[1:-1]
"""
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

#Solution 1,  compare the string and reversed string, if they are the same, then it is the Palindromic Substring
# Also this method need we adjust the start and end position of the string and reversed string
# slide it (faster than 32%)
class Solution(object):
    def max_samesub(self, s1,s2):
        while len(s1) >= 1:
            if s1 == s2:
                return s1
            else:
                if len(s1)>=2:
                    s1 = s1[1:-1]
                    s2 = s2[1:-1]
                else:
                    s1 = ''
        return ""
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""
        sr = s[::-1]
        max_str = ''
        for i in range(len(s)):
            str_left = self.max_samesub(s[i:],sr[:len(s)-i])
            str_right = self.max_samesub(s[:len(s)-i],sr[i:])                       
            if len(max_str) <= len(str_left):
                max_str = str_left
            if len(max_str) <= len(str_right):
                max_str = str_right
            
            
            if len(max_str) >= len(s[i:]):
                return max_str
        return max_str


#Solution 2, More faster (99.5%)
#Intuition: when you add a new char, you will only add 1 or 2 length to your longest Palindromatic string length
#suppose you add more than 2 length, then your longest Palindromatic substring is not longest
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s)==0:
        	return ""
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen] 
