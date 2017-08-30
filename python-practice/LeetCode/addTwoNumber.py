Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return_node = None
        carry = 0
        sum = 0
        while (l1 != None and l2 != None):
            sum = l1.val + l2.val + carry
            digit = sum % 10
            carry = sum / 10
            print(carry, digit)
            l1 = l1.next
            l2 = l2.next
            return_node = ListNode(digit)
            new_node = prev.next

        return new_node.next

[2,4,3]
[5,6,4]


test = Solution.addTwoNumbers()