from PrettyPrint import PrettyPrintTree


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return f"{self.value}"


class SplayTree:
    def __init__(self):
        self.root = None

    def _rotate(self, node, direction):
        if direction == 'left':
            other = node.rightChild
            node.rightChild = other.leftChild
            if other.leftChild:
                other.leftChild.parent = node
            other.leftChild = node
        else:  # direction == 'right'
            other = node.leftChild
            node.leftChild = other.rightChild
            if other.rightChild:
                other.rightChild.parent = node
            other.rightChild = node

        other.parent = node.parent
        node.parent = other
        if not other.parent:
            self.root = other
        else:
            if other.parent.leftChild == node:
                other.parent.leftChild = other
            else:
                other.parent.rightChild = other

    def leftRotate(self, node):
        self._rotate(node, 'left')

    def rightRotate(self, node):
        self._rotate(node, 'right')

    def performSplay(self, node):
        while node != self.root:
            if node.parent == self.root:
                if node == node.parent.leftChild:
                    self.rightRotate(node.parent)
                else:
                    self.leftRotate(node.parent)
            else:
                grandparent = node.parent.parent
                parent = node.parent
                if parent.leftChild == node and grandparent.leftChild == parent:
                    self.rightRotate(grandparent)
                    self.rightRotate(parent)
                elif parent.rightChild == node and grandparent.rightChild == parent:
                    self.leftRotate(grandparent)
                    self.leftRotate(parent)
                elif parent.rightChild == node and grandparent.leftChild == parent:
                    self.leftRotate(parent)
                    self.rightRotate(grandparent)
                else:
                    self.rightRotate(parent)
                    self.leftRotate(grandparent)

    def insert(self, value):
        newNode = TreeNode(value)
        temp = None
        currentNode = self.root
        while currentNode:
            temp = currentNode
            if newNode.value < currentNode.value:
                currentNode = currentNode.leftChild
            else:
                currentNode = currentNode.rightChild
        newNode.parent = temp
        if not temp:
            self.root = newNode
        elif newNode.value < temp.value:
            temp.leftChild = newNode
        else:
            temp.rightChild = newNode
        self.performSplay(newNode)

    def find(self, value):
        currentNode = self.root
        while currentNode and currentNode.value != value:
            if value < currentNode.value:
                currentNode = currentNode.leftChild
            else:
                currentNode = currentNode.rightChild
        if currentNode:
            self.performSplay(currentNode)
        return currentNode

    def printTree(self):
        def getChildren(node):
            children = []
            if node.leftChild:
                node.leftChild.isLeftChild = True
                children.append(node.leftChild)
            if node.rightChild:
                node.rightChild.isLeftChild = False
                children.append(node.rightChild)
            return children

        def getNodeValue(node):
            if hasattr(node, "isLeftChild"):
                direction = "L" if node.isLeftChild else "R"
                return f"{direction}: {str(node.value)}"
            return str(node.value)

        prettyPrint = PrettyPrintTree(getChildren, getNodeValue)
        prettyPrint(self.root)


if __name__ == "__main__":
    splayTree = SplayTree()
    while True:
        print("\nOperations:")
        print("1. Insert")
        print("2. Find")
        print("3. Quit")
        operation = input("Choose an operation: ")
        if operation == "1":
            value = int(input("Enter value to insert: "))
            splayTree.insert(value)
            splayTree.printTree()
        elif operation == "2":
            value = int(input("Enter value to find: "))
            result = splayTree.find(value)
            if result:
                print(f"Value {value} found.")
            else:
                print(f"Value {value} not found.")
            splayTree.printTree()
        elif operation == "3":
            break
        else:
            print("Invalid choice. Please choose again.")
