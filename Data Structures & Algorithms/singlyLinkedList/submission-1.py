

class ListNode:
    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.hidden_head = ListNode(-1)
        self.hidden_tail = self.hidden_head

    def get(self, index: int) -> int:
        current = self.hidden_head.next
        i = 0
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        next_node = self.hidden_head.next
        self.hidden_head.next = ListNode(val, next_node)

    def insertTail(self, val: int) -> None:
        current = self.hidden_head
        while current.next:
            current = current.next
        current.next = ListNode(val, None)

    def remove(self, index: int) -> bool:
        prev = self.hidden_head
        current = self.hidden_head.next
        i = 0
        while current and prev:
            if i == index:
                prev.next = current.next
                return True
            i += 1
            prev = prev.next
            current = current.next 

        return False
        

    def getValues(self) -> List[int]:
        current = self.hidden_head.next
        all_values = []
        while current:
            all_values.append(current.val)
            current = current.next
        return all_values
        
