# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = node = head
        len_of_list = 0
        while temp:
            len_of_list += 1
            temp = temp.next

        middle = len_of_list // 2
        counter = 0
        
        while node:
            if counter == middle:
                return node
            else:
                counter +=1
                node = node.next
        return None
