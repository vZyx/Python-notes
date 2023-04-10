class Solution(object):
    def hasCycle(self, head):   # O(n) time and O(n) memory
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next

        return False

    # This problem has O(n) time and O(1) memory solution
    # https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python