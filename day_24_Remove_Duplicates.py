class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        current = None
        if head is not None:
            current = head
            p = current
        while current is not None and current.next is not None:
            # p = current
            current = current.next
            # if p is not None:
            while current is not None and p.data == current.data:
                p.next = current.next
                current = current.next
            
            p = current
                # current = current.next
        self.display(head)
        # print(head.data)
        #Write your code here

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
