"""
problem description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

#Solution 1(my solution):
#function transfer from linkedlist to number then detransfer from number to linkedlist


import copy
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def transfer(self, li):
        resu = 0
        flag = 0
        while li != None:
            resu += li.val*10**flag
            flag += 1
            li = li.next
        return resu
#detransfer function makes deep copy
    def detransfer(self, num):
        hd = ListNode(0)
        for s in str(num):
            hd.val = int(s)
            hd.next = copy.copy(hd)
        return hd
    def detransfer2(self, num):
        hd = ListNode(0)
        new_hd = ListNode(0)
        for s in str(num):
            hd.val = int(s)
            new_hd.next = hd
            hd = copy.copy(new_hd)
        return hd.next
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        num1 = self.transfer(l1)
        num2 = self.transfer(l2)
        resu_num = num1 + num2
        return self.detransfer2(resu_num)


hd.val = int(s)
new_hd.next = hd
hd = new_hd # deep copy, change together

l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

#But first solution use 153ms to pass the test

#Solution 2, more direct way from natural think

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry = (carry)//10
        return dummyhead.next
# 1.dummy here is deep copy so we can remember the start position of the linked list
# 2.dont think carry setting be to complicated, just assign carry%10 to the val we want, and carry become carry//10
