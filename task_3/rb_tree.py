class Node:
    def __init__(self, value, left=None, right=None, parent=None, is_red=True):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.is_red = is_red

class RB_Tree:
    def __init__(self):
        self.root = None

    def grandpa(self, node):
        if node.parent:
            return node.parent.parent
        return None

    def uncle(self, node):
        g = self.grandpa(node)
        if not g or not node.parent:
            return None
        if g.left == node.parent:
            return g.right
        else:
            return g.left

    def insert(self, value):
        if not self.root:
            self.root = Node(value, is_red=False)
            return
        curnode = self.root
        while curnode:
            if value < curnode.value:
                if curnode.left:
                    curnode = curnode.left
                else:
                    curnode.left = Node(value=value, parent=curnode)
                    if curnode.is_red:
                        self.balance(curnode.left)
                        if self.root.is_red == True:
                            self.root.is_red = False
                    return
            else:
                if curnode.right:
                    curnode = curnode.right
                else:
                    curnode.right = Node(value=value, parent=curnode)
                    if curnode.is_red:
                        self.balance(curnode.right)
                        if self.root.is_red == True:
                            self.root.is_red = False
                    return

    def rotation(self, node, direction):
        if direction == "right":
            curnode = node.left
            curnode.parent = node.parent
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = curnode
                else:
                    node.parent.right = curnode
            else:
                self.root = curnode
            node.left = curnode.right
            if curnode.right:
                curnode.right.parent = node
            node.parent = curnode
            curnode.right = node
            return
        else:
            curnode = node.right
            curnode.parent = node.parent
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = curnode
                else:
                    node.parent.right = curnode
            else:
                self.root = curnode
            node.right = curnode.left
            if curnode.left:
                curnode.left.parent = node
            node.parent = curnode
            curnode.left = node
            return  

    def balance(self, start_node):
        parent_node = start_node.parent
        if not parent_node or parent_node.is_red == False:
            return
        uncle_node = self.uncle(start_node)
        grandpa_node = self.grandpa(start_node)
        if not uncle_node or uncle_node.is_red == False:
            if grandpa_node.left and start_node == grandpa_node.left.left:
                grandpa_node.is_red = True
                parent_node.is_red = False
                self.rotation(grandpa_node, "right")
                return
            elif grandpa_node.left and start_node == grandpa_node.left.right:
                grandpa_node.is_red = True
                start_node.is_red = False
                self.rotation(parent_node, "left")
                self.rotation(grandpa_node, "right")
                return
            elif grandpa_node.right and start_node == grandpa_node.right.left:
                grandpa_node.is_red = True
                start_node.is_red = False                
                self.rotation(parent_node, "right")
                self.rotation(grandpa_node, "left")
                return
            elif grandpa_node.right and start_node == grandpa_node.right.right:
                grandpa_node.is_red = True
                parent_node.is_red = False
                self.rotation(grandpa_node, "left")
                return
            else:
                return
        else:
            grandpa_node.is_red = True
            uncle_node.is_red = False
            parent_node.is_red = False
            self.balance(grandpa_node)
            return        

    def print_tree_rec_wide(self):
        self._print_tree_rec_wide([self.root])

    def _print_tree_rec_wide(self, nodes):
        if len(nodes) == 0:
            print("============")
            return
        node = nodes.pop(0)
        if node:
            print("value = ", node.value, "parent = ", node.parent.value if node.parent else "no parent", "color = ", node.is_red)
            nodes.append(node.left)
            nodes.append(node.right)
        self._print_tree_rec_wide(nodes)
