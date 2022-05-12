class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        pass

    def append(self, data_in):
        auxiliar_node = Node(data_in)
        auxiliar_node.next = self.head
        self.head = auxiliar_node

    def remove(self, data):
        head = self.head

        if (head is not None):
            if (head.data == data):
                self.head = head.next
                head = None
                return
        while (head is not None):
            if head.data == data:
                break
            prev = head
            head = head.next

        if (head == None):
            return

        prev.next = head.next
        head = None

    def show(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next
