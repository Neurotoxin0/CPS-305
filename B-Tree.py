class Node(object):
    def __init__(self, value):
        # values: up to three values
        self.value1 = value
        self.value2 = None
        self.value3 = None
        # children: up to four children
        self.lessthanv1 = None                                                              # first child: less than value 1
        self.v1v2 = None
        self.v2v3 = None
        self.largerthanv3 = None
        # parent
        self.parent = None

    def isLeaf(self):                                                                       # if no child: leaf => true
        return (self.lessthanv1 is None and self.v1v2 is None and self.v2v3 is None and self.largerthanv3 is None)

    def isFull (self):                                                                      # if value 3 is not empty => full
        return (self.value3 is not None)

    def ContainValue(self, value):                                                          # if current processing node have given value
        if self.value1 == value:
            return True
        elif self.value2 == value:
            return True
        elif self.value3 == value:
            return True
        else:
            return False

    def search(self, value):                                                                # search children
        if value < self.value1:
            return self.lessthanv1
        elif self.value1 < value and value < self.value2:
            return self.v1v2
        elif self.value2 < value and value < self.value3:
            return self.v2v3
        else:
            return self.largerthanv3

    def locate(self, node):                                                                 # used to determine which location the given node is locate (v1, v2, v3 or v4) and return its left child
        if self.node.parent.v1 == node:                                                     # used in balance()
            return node.lessthanv1
        elif self.node.parent.v2 == node:
            return node.v1v2
        elif self.node.parent.v3 == node:
            return node.v2v3
        else:
            return node.largerthanv3

    def status(self):                                                                       # return how many value the node is contain
        if self.isFull():
            return 3
        elif self.value2 != None:
            return 2
        else:
            return 1


class BTree(object):
    def __init__(self):
        self.RootNode = None


    def find(self, value):
        if not self.RootNode:
            return None
        else:
            return self.find_sub(self.RootNode, value)

    def find_sub(self, node, value):
        if not node:                                                                        # node not found
            return None
        elif node.ContainValue(value):                                                      # node found
            return node
        else:
            return self.find_sub(node.search(value), value)                                 # search children


    def insert(self, value):
        if not self.RootNode:
            self.RootNode = Node(value)
        else:
            self.insert_sub(self.RootNode, value)

    def insert_sub(self, node, value):
        if node.ContainValue(value):                                                        # value already exist
            return None
        elif node.isLeaf():                                                                 # leaf node => insert
            return self.insert_action(node, value)
        else:
            child = node.search(value)                                                      # not leaf child, find leaf child
            self.insert_sub(child, value)

    def insert_action(self, node, value):
        if node.isFull():                                                                   # full => split
            self.split(node, value)
        else:
            # do not exist v2:
            if not node.value2:
                if value < node.value1:                                                     # if given value is smaller than v1
                    node.value2 = node.value1
                    node.value1 = value
                else:                                                                       # given is larger
                    node.value2 = value
            # exist v2 => insert v3
            else:
                if value < node.value1:                                                     # value < v1
                    node.value3 = node.value2
                    node.value2 = node.value1
                    node.value1 = value
                elif node.value1 < value and value < self.RootNode.value2:                  # v1 < value < v2
                    node.value3 = node.value2
                    node.value2 = value
                else:                                                                       # value > v2
                    node.value3 = value


    def split(self, node, value):
        # reached root: only root node have no parent
        if not node.parent:
            NewNode = Node(node.value2)                                                     # split a new 'upper node'; use middle value as its v1
            NewRightChild = Node(node.value3)                                               # split a new 'right child node'; use v3 as its v1
            node.value2 = None                                                              # old node: erase v2, v3 (splitted)
            node.value3 = None
            # update these three node's role
            node.parent = NewNode                                                           # set old node's parent as the new upper node
            NewRightChild.parent = NewNode                                                  # set new right child node's parent
            self.RootNode = NewNode                                                         # set new upper node as the root node
            # link new root node's children
            NewNode.lessthanv1 = node
            NewNode.v1v2 = NewRightChild
            self.insert(value)                                                              # continue the insert progress

        # if have parent:
        else:
            UpperNode = node.parent                                                         # assign parent to a variable
            NewRightChild1 = Node(node.value3)                                              # split a new 'right child node'; use v3 as its v1
            self.insert_action(UpperNode, node.value2)                                      # insert middle value to the parent node; will split if full

            if (UpperNode.status()-1) == 1:                                                 # if parent USED to have 1 child (2 children now)(lessthanv1 linked; v1v2==node; v2v3 is None; largerthanv3 is None)
                UpperNode.v2v3 = NewRightChild1                                             # link v2v3 to the new right child
            else:                                                                           # if USED to have 2 children (3 children now)(largerthanv3 is None, others are all linked)
                UpperNode.largerthanv3 = NewRightChild1                                     # linke largerthanv3 to the new right child

            node.value2 = None                                                              # old node: erase v2, v3
            node.value3 = None
            self.insert(value)


    def delete(self, value):
        if not self.find(value):                                                            # if not find node
            print ("Value not found in the tree")
            return
        else:
            ProcessingNode = self.find(value)

            if ProcessingNode.isLeaf():                                                     # if deleting node is leaf
                '''Code can be simplified again, but how lazy I'm...'''
                if ProcessingNode.isFull():                                                 # if leaf is full (3): direct delete (2 left is OK)
                    if ProcessingNode.value3 == value:
                        ProcessingNode.value3 = None

                    elif ProcessingNode.value2 == value:
                        ProcessingNode.value2 = ProcessingNode.value3
                        ProcessingNode.value3 = None

                    else:
                        ProcessingNode.value1 = ProcessingNode.value2
                        ProcessingNode.value2 = ProcessingNode.value3
                        ProcessingNode.value3 = None

                elif ProcessingNode.value2 != None:                                         # elif 2 value in node: direct delete (1 left is OK)
                    if ProcessingNode.value2 == value:
                        ProcessingNode.value2 = None
                    else:
                        ProcessingNode.value1 = ProcessingNode.value2
                        ProcessingNode.value2 = None

                else:                                                                       # if leaf got 1 value: delete it; borrow from parent; see if parent have at least 1 value left
                    Parent = ProcessingNode.parent()
                    # v1 is the one need to delete: replace v1 with parent's last value
                    if Parent.isFull():
                        ProcessingNode.value1 = Parent.value3
                        Parent.value3 = None
                    elif Parent.value2 != None:
                        ProcessingNode.value1 = Parent.value2
                        Parent.value2 = None
                    else:
                        ProcessingNode.value1 = Parent.value1
                        Parent.value1 = None

                    #After borrow value with parent, check if parent and the node it borrow from is still have at least 1 value
                    self.balance(Parent)

            else:                                                                           # if deleting node is not Leaf: make it leaf node and delete => simplify: replace the deleting node with its left child's biggest value
                LendNode = ProcessingNode.locate(ProcessingNode)                            # use its left child's biggest value to replace the deleting node, and delete the deleting node
                size = ProcessingNode.status()
                if size == 3:
                    LendValue = LendNode.value3
                    LendNode.value3 = None
                elif size == 2:
                    LendValue = LendNode.value2
                    LendNode.value2 = None
                else:
                    LendValue = LendNode.value1
                    LendNode.value1 = None
                    self.balance(LendNode)                                                  # after replacing, LendNode have no value: borrow

                if ProcessingNode.value1 == value:
                    ProcessingNode.value1 = LendValue
                elif ProcessingNode.value2 == value:
                    ProcessingNode.value2 = LendValue
                else:
                    ProcessingNode.value1 = LendNode


    def balance(self, node):                                                                # node have no value: need to borrow from its parent/ left child
        if node.isLeaf():
            LendNode = node.parent                                                          # if node is leaf, parent node will be the LendNode (where it need to borrow from)
        else:
            LendNode = node.locate(node)                                                    # if node is parent node, locate() will return its left child as LendNode

        if not node.value1:
            if LendNode.isFull():
                node.value1 = LendNode.value3
                LendNode.value3 = None

            elif LendNode.value2:
                node.value1 = LendNode.value2
                LendNode.value2 = None

            else:                                                                           # if 'node borrow from'(LendNode) have no value after process: re-run the balance for LendNode
                node.value1 = LendNode.value1
                LendNode.value1 = None
                self.balance(LendNode)
        else:
            return