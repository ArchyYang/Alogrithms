class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth = 0
        nodes = {}
        self.inorderTraversal(root, depth, nodes)
        result = []
        keys = list(nodes)
        keys.sort()
        for i in range(len(keys)):
            temp = nodes[i]
            if i % 2 == 1:
                temp = temp[::-1]
            result.append(temp)
        return result
                
        
    def inorderTraversal(self, root, depth, nodes):
        if root == None:
            return 
        self.inorderTraversal(root.left, depth+1, nodes)
        if depth in nodes:
            nodes[depth].append(root.val)
        else:
            nodes[depth] = [root.val]
        self.inorderTraversal(root.right, depth+1, nodes)