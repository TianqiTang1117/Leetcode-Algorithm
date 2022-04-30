# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 检查是否为空
        if not inorder or not postorder:
            return None
        # 跟课上例题相似, 先找到root, 应该是后序遍历的最后一个元素
        rootVal = postorder[-1]
        # 创建根节点
        root = TreeNode(rootVal)
        # 用根节点的值去中序数组中查找对应元素下标
        midIndex = inorder.index(rootVal)
        # 找出中序遍历的左子树和右子树
        # 左子树区间为 [0,midIndex),右子树区间为[midIndex+1，n-1]
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex + 1:]
        # 找出后序遍历的左子树和右子树
        # 后序遍历和中序遍历的左子树和右子树长度相等，
        # 所以可以通过中序遍历左右子树的长度来确定后序遍历左右子树的位置
        postorderLeft = postorder[: len(inorderLeft)]
        postorderRight = postorder[len(inorderLeft): len(inorder) - 1]
        # 递归遍历左子树
        root.left = self.buildTree(inorderLeft, postorderLeft)
        # 递归遍历右子树
        root.right = self.buildTree(inorderRight, postorderRight)
        return root
