"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""

#Solution 1(faster than 27%)
#every_maxlen function to calculate the length of different chars from start
#then every time step ahead if two chars are not different, if they are same, start from the next to call every_maxlen
class Solution(object):
    def every_maxlen(self, s):
        dict_dif = {}
        every_maxlen_start = 0
        for i in range(len(s)):
            if s[i] not in dict_dif:
                dict_dif[s[i]] = 1
                every_maxlen_start += 1
            else:
                break   
        return every_maxlen_start
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dif = len(set(s))
        max_len = 1
        j = 0
        while j <= len(s)-2:
            if s[j+1] == s[j]:
                j += 1 
            else:
                max_len = max(max_len, self.every_maxlen(s[j:]))
                if max_len == dif:
                    max_len = dif
                    break
                j += 1
        return max_len

#Solution 2, faster (faster 77% than others)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longestSubLength = 0
        currentStart = 0
        lastSeen = dict()
        totalLength = len(s)
        for ix in range(totalLength):
            charCurrent = s[ix]
            if charCurrent in lastSeen and lastSeen[charCurrent] >= currentStart:
                if ix - currentStart > longestSubLength:
                    longestSubLength = ix - currentStart
                currentStart = lastSeen[charCurrent] + 1
            lastSeen[charCurrent] = ix
        if totalLength - currentStart > longestSubLength:
            longestSubLength = totalLength - currentStart
        return longestSubLength
        """
        :type s: str
        :rtype: int
        """
        
        
