from PrettyPrint import PrettyPrintTree


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}"

class SplayTree:
    def __init__(self):
        self.root = None

    def _leftRotate(self, x):
        # Rotate x to the left
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rightRotate(self, x):
        # Rotate x to the right
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def splay(self, node):
        while node != self.root:
            # Case: Node's parent is root (Zig or Zag)
            if node.parent == self.root:
                if node == node.parent.left:  # Zig rotation
                    self._rightRotate(node.parent)
                else:  # Zag rotation
                    self._leftRotate(node.parent)
            else:
                # Determine the grandparent
                grandparent = node.parent.parent
                parent = node.parent

                # Zig-Zig (Left-Left) Case
                if parent.left == node and grandparent.left == parent:
                    self._rightRotate(grandparent)
                    self._rightRotate(parent)
                # Zag-Zag (Right-Right) Case
                elif parent.right == node and grandparent.right == parent:
                    self._leftRotate(grandparent)
                    self._leftRotate(parent)
                # Zig-Zag (Left-Right) Case
                elif parent.right == node and grandparent.left == parent:
                    self._leftRotate(parent)
                    self._rightRotate(grandparent)
                # Zag-Zig (Right-Left) Case
                else:
                    self._rightRotate(parent)
                    self._leftRotate(grandparent)


    def insert(self, key):
        # Insert key into the tree
        node = Node(key)
        y = None
        x = self.root
        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        self.splay(node)

    def find(self, key):
        # Find a node with the given key
        x = self.root
        while x and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if x:
            self.splay(x)
        return x

    def print_tree(self):
        def get_children(node):
            children = []
            if node.left:
                node.left.is_left_child = True  # Annotate the node as a left child
                children.append(node.left)
            if node.right:
                node.right.is_left_child = False  # Annotate the node as a right child
                children.append(node.right)
            return children

        def get_value(node):
            if hasattr(node, "is_left_child"):
                child_direction = "L" if node.is_left_child else "R"
                return f"{child_direction}: {str(node.key)}"
            return str(node.key)

        pt = PrettyPrintTree(get_children, get_value)
        pt(self.root)











if __name__ == "__main__":
    tree = SplayTree()
    while True:
        print("\nOperations:")
        print("1. Insert")
        print("2. Find")
        print("3. Quit")
        choice = input("Choose an operation: ")
        if choice == "1":
            key = int(input("Enter key to insert: "))
            tree.insert(key)
            tree.print_tree()
        elif choice == "2":
            key = int(input("Enter key to find: "))
            result = tree.find(key)
            if result:
                print(f"Node {key} found.")
            else:
                print(f"Node {key} not found.")
            tree.print_tree()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")

