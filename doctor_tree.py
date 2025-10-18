# class DoctorNode:
#     pass
#     def __init__(self, name):
#         self.name = name
#         self.left = None
#         self.right = None
# 
# 
# class DoctorTree:
#     passS
#     def __init__(self):
#         self.root = None
# 
#     def insert(self, parent_name, child_name, side):
#         """Insert a new DoctorNode under a given parent on the given side ('left' or 'right')."""
#         if side not in ("left", "right"):
#             raise ValueError("Side must be 'left' or 'right'.")
# 
#         parent_node = self._find_node(self.root, parent_name)
#         if parent_node is None:
#             raise ValueError(f"Parent doctor '{parent_name}' not found in the tree.")
# 
#         new_node = DoctorNode(child_name)
#         if side == "left":
#             if parent_node.left is not None:
#                 raise ValueError(f"Parent '{parent_name}' already has a left report.")
#             parent_node.left = new_node
#         else:
#             if parent_node.right is not None:
#                 raise ValueError(f"Parent '{parent_name}' already has a right report.")
#             parent_node.right = new_node
# 
#     def _find_node(self, node, name):
#         """Helper to find a doctor by name."""
#         if node is None:
#             return None
#         if node.name == name:
#             return node
# 
#         left_result = self._find_node(node.left, name)
#         if left_result:
#             return left_result
# 
#         return self._find_node(node.right, name)
# 
#     def preorder(self, node):
#         """Root -> Left -> Right"""
#         if node is None:
#             return []
#         return [node.name] + self.preorder(node.left) + self.preorder(node.right)
# 
#     def inorder(self, node):
#         """Left -> Root -> Right"""
#         if node is None:
#             return []
#         return self.inorder(node.left) + [node.name] + self.inorder(node.right)
# 
#     def postorder(self, node):
#         """Left -> Right -> Root"""
#         if node is None:
#             return []
#         return self.postorder(node.left) + self.postorder(node.right) + [node.name]
# 
# if __name__ == "__main__":
#     tree = DoctorTree()
#     tree.root = DoctorNode("Dr. John")
#     tree.insert("Dr. John", "Dr. Sam", "right")
#     tree.insert("Dr. John", "Dr. Jose", "left")
#     tree.insert("Dr. Samclea", "Dr. Robert", "right")
#     tree.insert("Dr. Sam", "Dr. Gray", "left")
# 
#     print("Preorder:", tree.preorder(tree.root))
#     print("Inorder:", tree.inorder(tree.root))
#     print("Postorder:", tree.postorder(tree.root))




# Test your DoctorTree and DoctorNode classes here

class DoctorNode:

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:

    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        """Insert a new DoctorNode under a given parent on the given side ('left' or 'right')."""
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        parent_node = self._find_node(self.root, parent_name)
        if parent_node is None:
            raise ValueError(f"Parent doctor '{parent_name}' not found in the tree.")

        new_node = DoctorNode(child_name)
        if side == "left":
            if parent_node.left is not None:
                raise ValueError(f"Parent '{parent_name}' already has a left report.")
            parent_node.left = new_node
        else:
            if parent_node.right is not None:
                raise ValueError(f"Parent '{parent_name}' already has a right report.")
            parent_node.right = new_node

    def _find_node(self, node, name):
        """Helper to find a doctor by name."""
        if node is None:
            return None
        if node.name == name:
            return node

        left_result = self._find_node(node.left, name)
        if left_result:
            return left_result

        return self._find_node(node.right, name)

    def preorder(self, node):
        """Root -> Left -> Right"""
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        """Left -> Root -> Right"""
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        """Left -> Right -> Root"""
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]

if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. John")
    tree.insert("Dr. John", "Dr. Sam", "right")
    tree.insert("Dr. John", "Dr. Jose", "left")
    tree.insert("Dr. Sam", "Dr. Robert", "right")
    tree.insert("Dr. Sam", "Dr. Gray", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))