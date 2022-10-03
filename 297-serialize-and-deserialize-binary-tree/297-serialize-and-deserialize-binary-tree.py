# Definition for a binary tree node.
import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        # breadth first traversal, adding the values in left to right, levels order
        if not root: return '[]'
        l = []
        q = [root]
        for node in q: 
            if not node: 
                l.append("null")
                continue
            l.append(node.val)
            q.append(node.left if node.left else None)
            q.append(node.right if node.right else None)
        while l and l[-1] == "null":
            l.pop()
        return str(l).replace('\"', '').replace("\'", '').replace(' ', '')

    def deserialize(self, data:str):
        # deserialize leetcode's TreeNode format, this can help with future lt problems as well!
        if len(data) <= 2: return None # data must just have []
        l =  data[1:len(data)-1].split(',')

        q = queue.SimpleQueue()
        tr = TreeNode(int(l[0]))
        q.put((tr, "left"))
        q.put((tr, "right"))
        
        ptr = 1
        while ptr < len(l):
            root, direction = q.get()
            nextVal = l[ptr]
            if nextVal != "null": 
                newNode = TreeNode(int(nextVal))
                if direction == "left":
                    root.left = newNode
                else: 
                    root.right = newNode
                q.put((newNode, "left"))
                q.put((newNode, "right"))
            ptr += 1
        return tr


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# a = TreeNode(3)
# b = a.left = TreeNode(4)
# print(a, b)
# b.left = TreeNode(7)
# print(a, b)

deser = Codec()
serialized = "[]"
# ans = deser.deserialize("[1,2,3,null,null,4,5]")
print(deser.serialize(deser.deserialize(serialized)))
print(deser.serialize(deser.deserialize(serialized)) == serialized)