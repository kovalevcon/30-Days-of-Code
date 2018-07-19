class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head == None:
            return Node(data)

        if head.next == None:
            head.next = Node(data)
        else:
            self.insert(head.next, data)

        return head

mylist = Solution()
head = None
for data in [2, 3, 4, 1]:  # 2, 3, 4, 1
    head = mylist.insert(head, data)
mylist.display(head)  # 1 4 3 2
