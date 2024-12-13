# Definition for singly-linked list.
from typing import Optional
from math import log10
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        digit_count = -1
        total = 0
        while l1 is not None or l2 is not None:
            digit_count += 1
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            total += sum * (10**digit_count)
        digit_count = 0 if total == 0 else int(log10(total))
        f1 = ListNode(0, None)
        while total > 0:
            offload_num = total // (10**digit_count)
            f1.val = offload_num
            total_size = int(log10(total))
            total -= (offload_num * (10**digit_count))
            remaining_size = 0 if total == 0 else int(log10(total))
            if total_size - remaining_size == 1:
                new_node = ListNode(0, f1)
                f1 = new_node
                digit_count -= 1
                continue
            for i in range(total_size - remaining_size):
                digit_count -= 1
                new_node = ListNode(0, f1)
                f1 = new_node
        return f1




sol = Solution()
# l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3)))
# l2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 4)))
# l1 = ListNode(0, None)
# l2 = ListNode(0, None)
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9,None))))))) 
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
sol.addTwoNumbers(l1,l2)
