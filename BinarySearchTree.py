from re import T


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
        
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if node.value == temp.value:
                return False
            if node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.__dict__



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
print(my_tree.min_value_node(my_tree.root))
print(my_tree.min_value_node(my_tree.root.right))