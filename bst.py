

class BSTree():
    def __init__(self,value = None) -> None:
        # super().__init__(value)
        self.value = value
        self.left_node: BSTree = None
        self.rigth_node: BSTree = None

    def insert(self, value):
        if not self.value:
            self.value = value
        elif self.value == value:
            return
        elif value < self.value:
            if self.left_node:
                self.left_node.insert(value)
            else:
                self.left_node = BSTree(value)
        elif value > self.value:
            if self.rigth_node:
                self.rigth_node.insert(value)
            else:
                self.rigth_node = BSTree(value)

    def inorder(self):
        tree = []
        if self.left_node:
            tree += self.left_node.inorder()
        print (self.value,end=' ')
        tree.append(self.value)
        if self.rigth_node:
            tree += self.rigth_node.inorder()
        # print (tree)
        return tree

    def preorder(self):
        tree = [self.value]
        if self.left_node:
            tree += self.left_node.preorder()
        if self.rigth_node:
            tree += self.rigth_node.preorder()
        return tree
    
    def postorder(self):
        tree = []
        if self.left_node:
            tree += self.left_node.postorder()
        if self.rigth_node:
            tree += self.rigth_node.postorder()
        tree.append(self.value)
        return tree