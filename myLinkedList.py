#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Linked List Functionalities

Example:  1->2->6->3->4->5->6
'''


class ListNode:
    # Create New Node
    def __init__(self, value):
        self.val = value
        self.next = None


class myLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        #  add Node to end
        # print ("Append")
        newNode = ListNode(value)
        temp = self.head
        if temp is None:
            self.prepend(value)
        else:
            while temp.next:
                temp = temp.next
            temp.next = newNode
            newNode.next = None
        return self.head

    def prepend(self, value):
        # add Node to begining
        # print ("Prepend")
        newNode = ListNode(value)
        temp = self.head
        if temp is None:
            self.head = newNode
        else:
            self.head = newNode
            newNode.next = temp
        return self.head

    def insert(self, index, value):
        # add Node at index
        if index < 0:
            print ("Wrong index")
            return None
        if index == 0:
            return self.prepend(value)
        
        newNode = ListNode(value)
        temp = self.head
        for i in range(index - 1):
            if temp.next:
                temp = temp.next
            else:
                print("Index Error")
                return self.head
        newNode.next = temp.next
        temp.next = newNode
        return self.head

    def pop(self):
        # Delete the Node at end
        print("Pop")
        temp = self.head

        if temp is None:
            print("Empty LinkedList -- None")
        elif temp.next is None:
            print("Deleted ", temp.val)
            self.head = None
        else:
            while temp.next.next:
                temp = temp.next
            print("Deleted ", temp.next.val)
            temp.next = None

        return self.head

    def removeElementbyVal(self, value):
        # Remove element by value

        if self.head is None:
            print("Empty LinkedList -- No Val")
        else:
            dummy = ListNode(0)
            dummy.next = self.head
            temp = dummy
            found = False
            while temp and temp.next:
                if temp.next.val == value:
                    temp.next = temp.next.next
                    found = True
                    print(f'Value {value} Found')
                else:
                    temp = temp.next
            if not found:
                print("Value not Found")
        self.head = dummy.next
        return self.head

    def removeElementbyIndex(self, index):
        # Remove element by index
        if index < 0:
            print ("Wrong index")
            return None
        if self.head is None:
            print("Empty LinkedList -- No Index")
            return None
        # Index at begining
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                # Index can be out of range
                if temp and temp.next:
                    print("Value at index", _, "is: ", temp.val)
                    temp = temp.next
                else:
                    print("Index Error")
                    return self.head
            if temp.next is None:
                print("Index Error")
            else:
                print("Deleted", temp.next.val, "at", index)
                if temp.next.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
        return self.head

    def set_value(self, index, value):
        # Set value at Index

        if index < 0:
            print("Index ->", index, "Error")
            return None

        if self.head is None:
            print("Empty LinkedList")
            return None

        temp = self.head

        for _ in range(index):
            if temp and temp.next:
                temp = temp.next
            else:
                print("Index ->", index, "Error")
                return None
        print("Value at Index", index, "is:", temp.val)
        temp.val = value
        print("Changed Value at Index", index, "is:", temp.val)
        return self.head
    
    
    def reverseList(self):
        self.printLinkedList()
        # Reverse list
        if self.head is None:
            return None
        temp = self.head
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        self.head = before
        return self.head
            
            
            

    def printLinkedList(self):
        temp = self.head
        if temp is None:
            print("Empty LinkedList")
        else:
            while temp and temp.next:
                print(temp.val, "-> ", end=" ")
                temp = temp.next
            if temp:
                print(temp.val)



    

if __name__ == '__main__':
    linkedList = myLinkedList()
    nums = [1, 2, 3, 4, 5, 6]
    linkedList.printLinkedList()
    # TODO #
    # for num in nums:
    #     linkedList.append(num)
    # linkedList.printLinkedList()

    # append
    linkedList.append(10)
    linkedList.printLinkedList()
    linkedList.removeElementbyIndex(0)
    
    # prepend
    linkedList.prepend(100)
    linkedList.printLinkedList()

    # Insert
    linkedList.insert(1, 77)
    linkedList.printLinkedList()
    '''
    # pop
    set = 2
    for _ in range(set):
        linkedList.pop()
    linkedList.printLinkedList()

    # Remove by Value
    linkedList.removeElementbyVal(1)
    linkedList.printLinkedList()

    # Remove by Value
    linkedList.removeElementbyVal(100)
    linkedList.printLinkedList()

    # Remove by Value
    linkedList.removeElementbyVal(2)
    linkedList.printLinkedList()

    # Remove by Index
    linkedList.removeElementbyIndex(0)
    linkedList.printLinkedList()
    # linkedList.removeElementbyIndex(0)
    # linkedList.printLinkedList()
    # linkedList.removeElementbyIndex(0)
    # linkedList.printLinkedList()

    # append
    linkedList.append(10)
    linkedList.printLinkedList()

    # append
    linkedList.append(11)
    linkedList.printLinkedList()

    # Remove by Index
    linkedList.printLinkedList()
    linkedList.removeElementbyIndex(1)
    linkedList.removeElementbyIndex(1)
    linkedList.removeElementbyIndex(1)
    linkedList.removeElementbyIndex(1)
    linkedList.printLinkedList()

    # Remove by Index
    # linkedList.removeElementbyIndex(1)
    # linkedList.printLinkedList()

    # Insert Again
    for num in nums:
        linkedList.append(num)

    linkedList.printLinkedList()

    # Error Check
    linkedList.set_value(-1, 1)
    linkedList.set_value(20, 1)
    linkedList.set_value(7, 1)

    # Set Value
    linkedList.set_value(0, 1)
    linkedList.set_value(6, 1000)
    linkedList.printLinkedList()

    # Insert
    linkedList.insert(0, 2000)
    linkedList.printLinkedList()
    '''
    
    linkedList.reverseList()
    linkedList.printLinkedList()