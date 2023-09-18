from bst import BSTree
from random import randint


def test_bst():
    tree = BSTree()
    tree.insert(10)
    tree.insert(34)
    tree.insert(2)
    tree.insert(1)
    tree.insert(65)
    tree.insert(15)
    tree.insert(20)
    tree.insert(40)
    tree.insert(3)
    tree.insert(5)
    tree.insert(5)
    print("inorder:", end= ' ')
    print("\ninorder:", tree.inorder())
    print("preorder:", tree.preorder())
    print("postorder:", tree.postorder())


if __name__ =="__main__":
    test_bst()