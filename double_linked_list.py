class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        pass


class DoubleLinkedList():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        pass

    def isEmpty(self):
        return self.first == None

    def append(self, data):
        if self.isEmpty():
            self.first = self.last = Node(data)
        else:
            auxiliar_node = self.last
            self.last = auxiliar_node.next = Node(data)
            self.last.prev = auxiliar_node
        self.size += 1

    def prepend(self, data):
        if self.isEmpty():
            self.first = self.last = Node(data)
        else:
            auxiliar_node = Node(data)
            auxiliar_node.next = self.first
            self.first.prev = auxiliar_node
            self.first = auxiliar_node
        self.size += 1

    def at(self, index):
        if self.isEmpty() or not isinstance(index, int):
            return None
        else:
            curIndex = 0
            node = self.first
            while curIndex != index:
                print(node.next)
                if node.next == None:
                    return None

                node = node.next
                curIndex += 1
            return node

    def loop(self):
        auxiliar_node = self.first
        while auxiliar_node:
            print(auxiliar_node.data)
            auxiliar_node = auxiliar_node.next

    def loop_end(self):
        auxiliar_node = self.last
        while auxiliar_node:
            print(auxiliar_node.data)
            auxiliar_node = auxiliar_node.prev

    def delete_start(self):
        if self.isEmpty():
            return
        elif self.first.next == None:
            self.first = self.last = None
            self.size = 0
        else:
            self.first = self.first.next
            self.first.prev = None
            self.size -= 1

    def delete_last(self):
        if self.isEmpty:
            return
        elif self.first.next == None:
            self.first = self.last = None
            self.size = 0
        else:
            self.last = self.last.prev
            self.last.next = None
            self.size -= 1
