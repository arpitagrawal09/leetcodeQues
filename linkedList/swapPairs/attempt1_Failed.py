#Date : 18/07   Time taken : 4 hours
#No test cases passed at all. Tried the solution at leetcode but it does not seem to work 
#Work on the question picked up with the friend during the mock drill on 18/07
#Result : Not accepted. No idea about my code and logic
#Keywords : linked list, return head, swapping, swap nodes and not values 
#Leaving this probl to do dynamic programming 2nd question

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #print("starts")
        node = head
        while(node is not None):
            print(node.val) 
            node = node.next
        #print(head.val)
        #head = self.swapNewPairs(head, head, array = [])
        return head
            
    def swapNewPairs(self, head, starter, array):
        starter = head
        print("swapping starts")
        if starter.next is not None:
            initialFirst = starter.next
            if initialFirst.next is not None:
                initialSecond = initialFirst.next
                #pointerInitialFirst = initialFirst
                starter.next = initialSecond
                swappedFirst = starter.next
                if initialSecond.next is None:
                    swappedFirst.next = initialFirst
                    swappedSecond = swappedFirst.next
                    swappedSecond.next = None 
                    array.append(swappedFirst.val)
                    array.append(swappedSecond.val)
                    print(array)
                    return head 
                    #swapPairs(self, head, starter.next.next)
                else:
                    third = initialSecond.next
                    swappedSecond = initialFirst
                    #pointerSwappedFirst = swappedSecond
                    swappedSecond.next = third
                    swappedFirst.next = swappedSecond
                    starter = swappedSecond 
                    return -1
                    array.append(swappedFirst.val)
                    array.append(swappedSecond.val)
                    self.swapNewPairs(head, starter, array)
                    
            else:  
                return head 
        else: return head
