# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        current = head
        while list1 is not None or list2 is not None:
            if list1 is None:
                current.next = list2
                break
            elif list2 is None:
                current.next = list1
                break
            elif list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
        print_nodes(head)
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

input1 = [1,2,4]
input1a = [1,3,4]
input2 = []
input2a = []
input3 = []
input3a = [0]

# print_nodes(build_nodes(input1))
print(Solution().mergeTwoLists(build_nodes(input1), build_nodes(input1a)))
print(Solution().mergeTwoLists(build_nodes(input2), build_nodes(input2a)))
print(Solution().mergeTwoLists(build_nodes(input3), build_nodes(input3a)))
