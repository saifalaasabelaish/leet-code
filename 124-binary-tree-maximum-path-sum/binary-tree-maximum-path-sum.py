# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [root.val] #global variable

        def dfs(root):
            if not root:
                return 0            

            left_max_sum = dfs(root.left)    
            right_max_sum = dfs(root.right)
            
            left_max_sum = max(left_max_sum, 0)
            right_max_sum = max(right_max_sum, 0)

            result[0] = max(result[0], root.val + left_max_sum + right_max_sum) 

            return root.val + max(left_max_sum, right_max_sum)

        dfs(root)
        return result[0]
