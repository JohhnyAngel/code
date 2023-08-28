class ListNode:
    def __init__(self, val=0, next=None):
    # def __init__(self, val, next): 必须初始化，否则会报错
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head.next # 边界条件考虑极值，eg.index=0
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next) # 在Python中，赋值运算符是从右到左执行的。这意味着等式右边的表达式会先执行，然后将结果赋值给等号左边的变量或属性。也就是说先将self.dummy_head.next作为新加入节点的下一个节点，再将新加入节点赋值给self.dummy_head.next
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        for i in range(self.size):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: # 注意如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。所以不能用>=，用>
            return
        else:
            current = self.dummy_head
            for i in range(index):
                current = current.next
            current.next = ListNode(val, current.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: 
            return
        else:
            current = self.dummy_head
            for i in range(index):
                current = current.next
            current.next = current.next.next
            self.size -= 1

obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.deleteAtIndex(1)
param_1 = obj.get(1)