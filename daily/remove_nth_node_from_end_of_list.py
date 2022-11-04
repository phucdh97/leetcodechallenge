# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        count = -1
        arr = [(None, None)] * 30
        
        pre = None
        cur = head
        while cur is not None:
            count += 1
            arr[count] = (pre, cur)
            pre = cur
            cur = cur.next
        # print(arr)
        position = count+1 - n # arr from index 0
        # print("position: ", position)
        pre, node = arr[position]
        # print("value: ", arr[position])
        if pre is not None:
            pre.next = node.next
        else:
            dummy = node.next
        return dummy
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        count = 0
        pre_index = 0
        cur = head
        pre = None
        while cur is not None:
            count += 1
            if count - pre_index > n:
                pre_index += 1
                if pre is None:
                    pre = head
                else:
                    pre = pre.next
            cur = cur.next

        if pre is None:
            return head.next

        node = pre.next
        pre.next = node.next
        return head
        
sol = Solution()
sol.removeNthFromEnd()
        
            