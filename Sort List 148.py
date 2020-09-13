# https://leetcode.com/problems/sort-list/

# merge-sort with divide and conquer
# if it was just a list, it could be kept dividing half till the base case returns and then
# combine from there

# but it's a linked list.
# maybe I can make use of the same approach here?

# first try
# find the half point by iteration
# then, cut the list in half (left / right) recursively till the base case
# next, make a dummy node with another indicator (for the return function later)

# while both linked lists are not none
# compare left val and right val, then add the smaller to next dummy
# then move the pointer of the added node to the next node
# move the pointer of the dummy node to the next node

# return the next of another indicator

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head

        total_length = 0

        # while head:
        #     head = head.next
        #     total_length += 1

        iterator = head

        while iterator:
            iterator = iterator.next
            total_length += 1

        mid = total_length // 2

        left = left_iterator = head

        for _ in range(mid):
            left_iterator = left_iterator.next

        right = left_iterator.next
        left_iterator.next = None

        left_half = self.sortList(left)
        right_half = self.sortList(right)
        return self.merge(left_half, right_half)

    def merge(self, linked_1, linked_2):
        indicator = dummy = ListNode()
        left = linked_1
        right = linked_2

        while left and right:
            if left.val < right.val:
                dummy.next = ListNode(left.val)
                dummy = dummy.next
                left = left.next
            else:
                dummy.next = ListNode(right.val)
                dummy = dummy.next
                right = right.next

        if left or right:
            dummy.next = left or right

        return indicator.next

# result: AttributeError: 'NoneType' object has no attribute 'next'
# the pointer, head already reached None so left = left_iterator = head was meaning None
# corrected the line but still got Recursion Error (maximum recursion depth exceeded in comparison)
# AHHH if sky was the limit (I mean it the question doesn't require using constant space complexity,
# it could've been done with ease like switch a linked list to a normal list(an array), sort and then combine back
# anyways I'll have another try later



