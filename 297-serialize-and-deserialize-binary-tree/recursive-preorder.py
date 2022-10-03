# Definition for a binary tree node.
import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        l = []
        def recur(root): 
            if root is None: 
                l.append("null") 
                return
            l.append(str(root.val))
            recur(root.left)
            recur(root.right)
        recur(root)
        print(l)
        return ' '.join(l)
        

    def deserialize(self, data: str):
        # deserialize leetcode's TreeNode format, this can help with future lt problems as well!

        def recur(): 
            val = next(nodeIter)
            if val == 'null': 
                return None 
            root = TreeNode(val)
            root.left = recur()
            root.right = recur()
            return root
        nodeIter = iter(data.split())
        return recur()      


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
serialized = "[1,2,3,null,null,4,5,null,null,null,null]"
# ans = deser.deserialize("[1,2,3,null,null,4,5]")
print(deser.serialize(deser.deserialize(serialized)))
