class Node:
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.parent = parent

        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value, None)
        else:
            return recursive_insert(self.root, key, value)

    def traverse(self, callback):
        recursive_traverse(self.root, callback)

    def find(self, key):
        return recursive_find(self.root, key)


def recursive_insert(node, key, value):
    if key < node.key:
        if node.left_child is None:
            node.left_child = Node(key, value, node)

        else:
            return recursive_insert(node.left_child, key, value)

    elif key > node.key:
        if node.right_child is None:
            node.right_child = Node(key, value, node)
        else:
            return recursive_insert(node.right_child, key, value)
    else:
        value_to_throw = node.value
        node.value = value
        return value_to_throw


def recursive_traverse(node, visit):
    if node.left_child is not None:
        recursive_traverse(node.left_child, visit)

    visit(node.key, node.value)

    if node.right_child is not None:
        recursive_traverse(node.right_child, visit)


def recursive_find(node, key):
    if key > node.key:
        return recursive_find(node.right_child, key)
    elif key < node.key:
        return recursive_find(node.left_child, key)
    else:
        return node.value


if __name__ == '__main__':
    tree = Tree()
    tree.insert(4, "is a cosmic number")
    tree.insert(42, "is the life, universe, and everything")
    print(tree.insert(21, "What is nine plus ten"))
    tree.insert(3, "illuminati will find you")
    print(tree.insert(21, "What is 38 minus 17"))

    tree.traverse(print)

    print(tree.find(21))
