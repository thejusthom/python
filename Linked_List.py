class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail


class LinkedList:
    def __init__(self, *start):
        self.head = None
        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        self.head = LinkedNode(value, self.head)

    def remove(self, value):
        n = self.head
        last = None
        while n is not None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                    return True
            last = n
            n = n.next
        return False

    def pop(self):
        if self.head is None:
            raise Exception('List is empty')
        value = self.head.value
        self.head = self.head.next
        return value

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

    def __repr__(self):
        for _ in self:
            print(_)    

l = LinkedList()
l.prepend(5)
l.prepend(4)
l.prepend(7)
l.prepend(2)
l.remove(0)
l.pop()
for _ in l:
    print(_)