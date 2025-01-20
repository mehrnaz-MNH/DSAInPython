
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]



# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
#  * };
#  */
# class Solution {
# public:

#     int find_height(TreeNode * root)
#     {
#         if(root==NULL)
#         {
#             return 0;
#         }
#         return max(find_height(root->left),find_height(root->right))+1;
#     }
#     bool isBalanced(TreeNode* root)
#     {
#         if(root==NULL)
#         {
#             return true ;
#         }
#         int l = find_height(root->left);
#         int r = find_height(root->right);

#          return abs(l - r) <= 1 && isBalanced(root->left) && isBalanced(root->right);

#     }
# };
