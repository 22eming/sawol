from typing import DefaultDict
import sys
sys.setrecursionlimit(10**6)

result = []


class Node(object):
    def __init__(self, x, data):
        self.data = data
        self.x = x
        self.left = self.right = None


class BinaryTree(object):
    global result

    def __init__(self, root):
        self.root = root

    def insert(self, x, data):
        self.cur_node = self.root
        while True:
            if x < self.cur_node.x:
                if self.cur_node.left == None:
                    self.cur_node.left = Node(x, data)
                    break
                else:
                    self.cur_node = self.cur_node.left
            else:
                if self.cur_node.right == None:
                    self.cur_node.right = Node(x, data)
                    break
                else:
                    self.cur_node = self.cur_node.right
    # 전위순회

    def preorder(self, n):
        if n != None:
            result.append(n.data)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
    # 후위 순회

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            result.append(n.data)


def solution(nodeinfo):
    answer = []
    t = DefaultDict(list)
    root = [0, 0, 0]
    if len(nodeinfo) == 1:
        return [[1], [1]]
    for i, node in enumerate(nodeinfo, 1):
        x, y = node
        if root[0] < y:
            root = [y, x, i]
        t[y].append([x, i])
    root = Node(root[1], root[2])
    tree = BinaryTree(root)
    for y in sorted(t.keys(), reverse=True)[1:]:
        for x in t[y]:
            tree.insert(x[0], x[1])
    global result
    tree.preorder(root)
    answer.append(result)
    result = []
    tree.postorder(root)
    answer.append(result)
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
      [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
