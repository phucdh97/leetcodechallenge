from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        dummy = head

        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy

    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        m = n - d
        if m < 0:
            return -1
        dp = [[0]*(m + 1) for _ in range(d)]
        for j in range(m + 1):
            dp[0][j] = max(jobDifficulty[:j+1])
        for i in range(1, d):
            for j in range(m + 1):
                dp[i][j] = min([dp[i - 1][k] + max(jobDifficulty[i + k : i + j + 1])
                                for k in range(j + 1)])
        return dp[d - 1][m]