# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val >= list2.val:
            list2_rest = list2.next
            list2.next = list1
            return self.mergeTwoLists(list2, list2_rest)
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
                
        