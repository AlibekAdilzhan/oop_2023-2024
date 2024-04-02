class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"


class Tree:
    def __init__(self):
        self.root = None

def bfs(t: Tree):
    queue = [t.root]
    while queue != []:
        v = queue.pop(0)
        print(v.value)
        if v.left is not None:
            queue.append(v.left)
        if v.right is not None:
            queue.append(v.right)


#     5
#    / \
#   1   6
#  /\   /\
# 3  2    

t = Tree()
t.root = Node(5)
t.root.left = Node(1)
t.root.right = Node(6)
t.root.left.left = Node(3)
t.root.left.right = Node(2)

bfs(t)
