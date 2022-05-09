class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def append(self, value):
        node = Node(value)
        if self.lenght == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.lenght += 1
        return True

    def preappend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.lenght += 1

    def pop_first(self):
        if self.lenght == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.lenght -= 1
        temp.next = None
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp.__dict__

    def insert(self, value):
        pass

    def pop(self):
        if self.lenght == 0:
            return None
        else:
            temp = self.head
            pre = self.head

            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.lenght -= 1
            if self.lenght == 0:
                self.head = None
                self.tail = None
        return temp.__dict__

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index < 0 or index >= self.lenght:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        if index < 0 or index > self.lenght:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next

        temp.value = value
        return temp.__dict__


my_linked_list = LinkedList(4)
my_linked_list.append(7)
my_linked_list.preappend(22)
my_linked_list.append(8)
my_linked_list.preappend(15)
my_linked_list.preappend(999)
print('\nThe length is:', my_linked_list.lenght)
