class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isLeaf(self):
        if (self.left is None) and (self.right is None):
            return True
        return False

    def isFull(self):
        if (self.left is not None) and (self.right is not None):
            return True
        return False


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        """ if node is empty, default at root"""

        if self.root is None:
            return True
        return False

    def findMin(self, start):

        while start.left is not None:
            start = start.left

        return start.data

    def findMax(self, start):
        while start.right is not None:
            start = start.right

        return start.data

    def insert(self, data):

        node = BSTNode(data)

        if self.is_empty():
            self.root = node
        else:
            pointer = self.root

            while True:
                if node.data < pointer.data:
                    # go left
                    if pointer.left is None:
                        pointer.left = node
                        break
                    else:
                        pointer = pointer.left

                # node.data >= pointer.data
                else:
                    # go right
                    if pointer.right is None:
                        pointer.right = node
                        break
                    else:
                        pointer = pointer.right

    def traverse(self):
        print("-----")
        # print("Preorder:", end=" ")
        self.preorder(self.root)
        print()

        # print("Inorder =", end=" ")
        self.inorder(self.root)
        print()

        # print("Postorder =", end=" ")
        self.postorder(self.root)
        print()

    def preorder(self, start):
        if start == self.root:
            print("Preorder :", end=" ")
        if start is not None:
            print("->", start.data, end=" ")
            self.preorder(start.left)
            self.preorder(start.right)

    def inorder(self, start):
        if start == self.root:
            print("Inorder :", end=" ")
        if start is not None:
            self.inorder(start.left)
            print("->", start.data, end=" ")
            self.inorder(start.right)

    def postorder(self, start):
        if start == self.root:
            print("Preorder :", end=" ")

        if start is not None:
            self.postorder(start.left)
            self.postorder(start.right)
            print("->", start.data, end=" ")

    def insertMultiple(self, lst):

        for i in lst:
            self.insert(i)

    def delete(self, target):
        # target is number

        if self.is_empty():
            return None

        # delete root
        if target == self.root.data:
            if self.root.isLeaf():
                self.root = None

            elif self.root.isFull():

                x = self.findMax(self.root.left)
                self.delete(x)
                self.root.data = x

            elif self.root.left is not None:
                self.root = self.root.left

            elif self.root.right is not None:
                self.root = self.root.right

        else:
            pointer = self.root
            prev = pointer

            while True:

                if target < pointer.data:
                    # move pointer
                    prev = pointer
                    pointer = pointer.left

                    if pointer is None:
                        # cant find target
                        return None

                    # find target
                    if target == pointer.data:

                        if pointer.isLeaf():
                            prev.left = None
                        elif pointer.isFull():

                            x = self.findMax(pointer.left)
                            self.delete(x)
                            prev.left.data = x

                        # only left child
                        elif pointer.left is not None:
                            prev.left = pointer.left

                        elif pointer.right is not None:
                            prev.right = pointer.right

                else:
                    # move pointer
                    prev = pointer
                    pointer = pointer.right

                    if pointer is None:
                        # cant find target
                        return None

                    # find target
                    if target == pointer.data:

                        if pointer.isLeaf():
                            prev.right = None

                        elif pointer.isFull():
                                
                            x = self.findMax(pointer.left)
                            self.delete(x)
                            prev.right.data = x

                        # only left child
                        elif pointer.left is not None:
                            prev.left = pointer.left

                        elif pointer.right is not None:
                            prev.right = pointer.right

    def deleteMultiple(self, lst):

        for i in lst:
            self.delete(i)


bst = BST()
bst.insertMultiple((14, 23, 7, 10, 33))
bst.traverse()

bst.delete(14)
bst.traverse()

bst.insert(21)
bst.traverse()

bst.delete(23)
bst.traverse()

bst.insertMultiple((20,8,12))
bst.traverse()

bst.delete(20)
bst.traverse()

bst.insertMultiple((6,9))
bst.traverse()

bst.delete(10)
bst.traverse()