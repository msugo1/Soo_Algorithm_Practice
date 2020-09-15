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

# what I could come up with - slow and fast runner - what I've seen before
# slow runner moves once(next), whilst fast runner moves twice(next, next)
# when fast runner reaches the end, slow runner should be in the middle

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head

        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        left_half = self.sortList(head)
        right_half = self.sortList(slow)

        return self.merge(left_half, right_half)


    def merge(self, linked_1, linked_2):
        if linked_1 and linked_2:
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

            if left:
                dummy.next = left
            else:
                dummy.next = right

            return indicator.next

        # and

    def merge(self, linked_1, linked_2):
        if linked_1 and linked_2:
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

# when merge is 1, runtime: 548m/s
# when 2, runtime: 440m/s

    def merge(self, linked_1, linked_2):
        if linked_1 and linked_2:
            indicator = dummy = ListNode()

            while linked_1 and linked_2:
                if linked_1.val < linked_2.val:
                    dummy.next = linked_1
                    linked_1 = linked_1.next
                else:
                    dummy.next = linked_2
                    linked_2 = linked_2.next
                dummy = dummy.next

            dummy.next = linked_1 or linked_2

            return indicator.next

# unnecessary process has just gotten removed
# runtime also took a dive to 248m/s
# dummy node's next doesn't have to be created but only designated next as left or right whichever has lower value
# why? pointers for left and right keep moving and then dummy next will be replaced with either
# at the end just add whichever is left to dummy.next (if conditions is not necessary because it won't be added if none exists)

# code from Python Algorithm Interview
    def merge(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge(l1.next, l2)

        return l1 or l2

# runtime: 332 m/s
# guess it's because it's not creating new node but only swap l1, l2 by the condition

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        lst: List = []

        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head

# linked to list, sort and list to linked
# runtime: 88m/s (98.61%), memory usage: 21.3(98.80%)
# python sort is implemented by tim sort in C so the fastest but also the most memory-efficient way