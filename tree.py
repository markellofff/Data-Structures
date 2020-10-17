from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_traversal(self.root, [])
        elif traversal_type == 'postorder':
            return self.postorder_traversal(self.root, [])
        elif traversal_type == 'inorder':
            return self.inorder_traversal(self.root, [])
        elif traversal_type == 'levelorder':
            return level_order_traversal(self.root, [])
        else:
            return f"{traversal_type} is not supported"

    def preorder_traversal(self, root, result):
        """ Root -> Left -> Right"""
        if root:
            result.append(root.value)
            self.preorder_traversal(root.left, result)
            self.preorder_traversal(root.right, result)
        return result

    def postorder_traversal(self, root, result):
        """ Left -> Roght -> Root"""
        if root:
            self.postorder_traversal(root.left, result)
            self.postorder_traversal(root.right, result)
            result.append(root.value)
        return result

    def inorder_traversal(self, root, result):
        """ Left -> Root -> Right"""
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.value)
            self.inorder_traversal(root.right, result)
        return result

    def level_order_traversal(self, root, result):
        if root is None:
            return

        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            result.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result


# adding data in Binary Tree
bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

# 1, 2, 4, 5, 3, 6, 7
print(bt.print_tree('preorder'))
# 4 2 5 1 6 3 7
print(bt.print_tree('inorder'))
# 4 S 2 6 7 3 1
print(bt.print_tree('postorder'))
# 1 2 3 4 S 6 7
print(bt.print_tree('levelorder'))
