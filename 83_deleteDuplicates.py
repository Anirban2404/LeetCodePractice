''' 
Given the head of a sorted linked list, delete all duplicates such 
that each element appears only once. Return the linked list sorted as well.


Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3] 
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
class myLinkedList:
    
    def inputListNode(self,numbers): 
        # Now convert that list into linked list
        if len(numbers) <= 0:
            return None
        head = ListNode(numbers[0])
        ptr = head
        
        for number in numbers[1:]:
            ptr.next = ListNode(number)
            ptr = ptr.next
        
        ptr = head
        return head
        
    def printLinkedList(self,node):
        while node and node.next:
            print(str(node.val) + "->", end='')
            node = node.next
        if node:
            print(node.val)
        else:
            print("Empty LinkedList")

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
            
            
    
linkedList = myLinkedList()
numbers = [4,4,4,5,5]
head = linkedList.inputListNode(numbers)
linkedList.printLinkedList(head)
reultLL = Solution().deleteDuplicates(head)
linkedList.printLinkedList(reultLL)