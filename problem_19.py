# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead = head
        lag = head
        for _ in range(n):
            lead = lead.next
        if lead is None:
            return head.next
        while lead.next is not None:
            lead = lead.next
            lag = lag.next
        lag.next = lag.next.next
        return head
        

def build_nodes(input: list[int]) -> Optional[ListNode]:
    if len(input) == 0:
            return None
    else:
        head = ListNode(input[0])
    current = head
    for i in range(len(input)):
        if i < len(input) - 1:
            current.next = ListNode(input[i+1])
            current = current.next
    return head

def print_nodes(input: ListNode):
    while input is not None:
        print(input.val)
        input = input.next

input1 = [1,2,3,4,5]
input1a = 2
input2 = [1]
input2a = 1
input3 = [1,2]
input3a = 1

# print_nodes(build_nodes(input1))
print(Solution().removeNthFromEnd(build_nodes(input1), input1a))
print(Solution().removeNthFromEnd(build_nodes(input2), input2a))
print(Solution().removeNthFromEnd(build_nodes(input3), input3a))
