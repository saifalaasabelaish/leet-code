# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            depth = []
            next_queue = []

            for i in queue:
                depth.append(i.val)
                if i.left:
                    next_queue.append(i.left)
                if i.right:
                    next_queue.append(i.right)

            result.append(depth)
            queue = next_queue

        return result
        