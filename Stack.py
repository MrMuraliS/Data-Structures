from tkinter.messagebox import NO


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        node = Node(value)
        self.top = node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        node = Node(value)
        if self.height == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp


my_stack = Stack(5)
my_stack.push(4)
print(my_stack.pop())
my_stack.print_stack()
