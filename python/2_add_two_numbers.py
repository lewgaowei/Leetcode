from typing import Optional
from time import sleep

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry 
            
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next 
            

if __name__ == "__main__":
    sol = Solution()
    
    # Test case: 342 + 465 = 807 (represented as 2->4->3 + 5->6->4 = 7->0->8)
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    result = sol.addTwoNumbers(l1, l2)
    
    # Print result
    while result:
        print(result.val, end="")
        result = result.next
        if result:
            print("->", end="")
    print()
