class BST():
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            print("double data not allows")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self,data):
        if self.key ==data:
            print("node is found!")
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in Tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present!")

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")


    def delete(self,data,curr):
        if self.key is None:
            print("Tree is empty!")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print("given node is not present in Tree!")
        elif data> self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print("given Node is not present in Tree!")
        else:
            if self.lchild is None:
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return self
            if self.rchild is None:
                temp=self.lchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,curr)
        return self
 
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("Node with samllest key is",current.key)
    
    
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("Node with maximum key is",current.key)

def cout(node):
    if node is None:
        return 0
    return 1+cout(node.lchild)+cout(node.rchild)            

root=BST(10)
print(root.key)
list1=[12,1,5,3,70,90]
for i in list1:
    root.insert(i)
if cout(root)>1:
    root.delete(12,root.key)
else:
    print("can't perform deletions opertions!")
print("preorder")
root.preorder()
print()
print("Inorder")
root.inorder()
print()
print("postorder")
root.postorder()

print()
print(cout(root))
root.min_node()
root.max_node()