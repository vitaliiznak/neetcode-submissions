class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)      # dummy head
        self.tail = ListNode(0)      # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.head.next
        for _ in range(index):
            if curr == self.tail or curr is None:
                return -1
            curr = curr.next
        if curr == self.tail or curr is None:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        curr = self.head
        for _ in range(index):
            if curr.next == self.tail:
                return          # index too large
            curr = curr.next
        
        new_node = ListNode(val)
        new_node.prev = curr
        new_node.next = curr.next
        curr.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        curr = self.head
        for _ in range(index):
            if curr.next == self.tail or curr.next is None:
                return
            curr = curr.next
        if curr.next == self.tail or curr.next is None:
            return
        
        target = curr.next
        curr.next = target.next
        if target.next:
            target.next.prev = curr