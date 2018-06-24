# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        stack = [root]
        old_stack = [root]

        while len(stack) > 0:
            level = []
            old_stack = stack[:]
            stack = []
            for n in old_stack:
                level.append(n.val)
                if n.left != None:
                    stack.append(n.left)
                if n.right != None:
                    stack.append(n.right)
            result.append(level)

        return result

