# 13 7 15 3 8 14 19 18

#    13
#  /    \
# None   None

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def bfs(node: Node):
    q = [node]
    while q != []:
        curr = q.pop(0)
        print(curr.data)
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)


def insert(node: Node, data: int):
    if node is None:
        return Node(data)
    else:
        if data > node.data:
            node.right = insert(node.right, data)
        elif data < node.data:
            node.left = insert(node.left, data)
    return node


def search(node: Node, data: int):
    if node is None:
        return False
    else:
        if data == node.data:
            return True
        elif data > node.data:
            return search(node.right, data)
        elif data < node.data:
            return search(node.left, data)

def get_min(node: Node):
    if node is None:
        return None
    else:
        if node.left is None:
            return node.data
        else:
            return get_min(node.left)


root = Node(13)
my_list = [7, 15, 3, 8, 14, 19, 18]
for x in my_list:
    insert(root, x)

print(get_min(root))
