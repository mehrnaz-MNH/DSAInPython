from operator import contains


class Node :
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree :
    def __init__(self):
        self.root = None


    def insert_helper(self , root , value):
        if root is None:
            return Node(value)

        if value < root.value:
                root.left = self.insert_helper(root.left , value)
        if value > root.value :
                root.right = self.insert_helper(root.right, value)

        return root


    def insert(self, value):
        if self.root is None :
            self.root = Node(value)
        self.insert_helper(self.root, value)



    def contains_helper(self , root , value):
        if root is None:
            return False

        if value == root.value:
                return True
        if value < root.value:
                return self.contains_helper(root.left , value)
        else:
                return self.contains_helper(root.right, value)

    def contains(self, value):
        return self.contains_helper(self.root , value)


    def min_value(self , c_node):
        while c_node.left is not None :
            c_node = c_node.left

        return c_node.value


    def delete_helper(self , root , value):
        if root is None :
            return None

        if value < root.value :
            root.left = self.delete_helper(root.left, value)
        elif value > root.value :
            root.right = self.delete_helper(root.right , value)

        else :
            if root.left is None and root.right is None:
                return None
            elif root.left is None :
                root = root.right
            elif root.right is None :
                root = root.left
            else :
                sub_tree_min = self.min_value(root.right)
                root.value = sub_tree_min
                root.right = self.delete_helper(root.right , sub_tree_min)

        return root


    def delete(self , value):
        self.delete_helper(self.root , value)


    def BFS(self):
        c_node = self.root
        queue = []
        results = []
        queue.append(c_node)
        while len(queue) > 0 :
            c_node = queue.pop(0)
            results.append(c_node.value)
            if c_node.left is not None :
                queue.append(c_node.left)

            if c_node.right is not None :
                queue.append(c_node.right)

        return results

    def dfs_pre_order(self):
        results = []
        def traverse(c_node):
            results.append(c_node.value)
            if c_node.left is not None :
                traverse(c_node.left)
            if c_node.right is not None :
                traverse(c_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []
        def traverse(c_node):
            if c_node.left is not None :
                traverse(c_node.left)
            if c_node.right is not None :
                traverse(c_node.right)
            results.append(c_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(c_node):
            if c_node.left is not None:
                traverse(c_node.left)
            results.append(c_node.value)
            if c_node.right is not None:
                traverse(c_node.right)


        traverse(self.root)
        return results




















