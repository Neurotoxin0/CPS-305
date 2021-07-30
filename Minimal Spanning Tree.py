''' NOT FULLY FUNCTIONING => bug occur during adding'''
''' Code is theoretically meet all required requirements'''

import re

class Vertices(object):                                                 # used to store vertices with its value, node tthat ie linked to and their weights
    def __init__(self, value, link, weight):
        self.value = value
        self.link = []

        if (link is not None) and (weight is not None):                 # if given is not a empty node: create link and weight
            self.link.append([link, weight])                            # empty node is often given when a node itself is only linked but have no link to other node
                                                                        # eg: 1 3 4, where node 1 link to 3, weight is 4; but node 3 is empty and have no link or weight

class MST(object):
    def __init__(self):
        self.init = None                                                # first node added, use it to go through all nodes
        self.list = []                                                  # list of all existing nodes
        self.weight = []                                                # list of all existing weights


    def find(self, value, weight):                                      # return a node is found; can used to find value or weight
        if not self.init:
            return None
        elif weight is None:                                            # if is finding specific value
            return self.find_sub(self.init, value, None)

        elif value is None:                                             # if is finding specific weight
            return self.find_sub(self.init, None, weight)

    def find_sub(self, node, value, weight):
        if weight is None:                                              # find value
            if node.value == value:
                return node
            else:
                if len(node.link) != 0:                                 # while current node linked to other node: check other node for value
                    for link in node.link:
                        return self.find_sub(link[0], value, None)

                return None

        elif value is None:                                             # find weight
            if len(node.link) != 0:
                for link in node.link:
                    #print(link[1], weight, type(link[1]), type(weight)) #debug code
                    if link[1] == weight:
                        return node

            for link in node.link:                                      # while current node linked to other node: check other node for weight
                return self.find_sub(link[0], None, weight)

            return None


    def insert(self, value, link, weight):
        if not self.init:
            LinkNode = Vertices(link, None, None)                       # create the node that need to be linked first
            NewNode = Vertices(value, LinkNode, int(weight))            # create node and pass the linked node and weight to the new node
            self.init = NewNode
            self.list.append(int(value))                                # append added node's value
            self.list.append(int(link))                                 # append linked node to the list too
            self.weight.append(int(weight))                             # append added node's weight

        elif self.find(value, None) is not None:                        # if the node need to add DO exist
            #print("node found")    # debug code
            node = self.find(value, None)

            if self.find(link, None) is not None:                       # add linked node to the existing node
                LinkNode = self.find(link, None)                        # check if the linked node already exist: if no, create it
                print("link node found")
            else:
                LinkNode = Vertices(link, None, None)
                print("link node not found")

            node.link.append([LinkNode, int(weight)])                   # append added node's value
            self.list.append(int(link))                                 # append linked node to the list too
            self.weight.append(int(weight))                             # append added node's weight

        else:                                                           # if the node need to add DO NOT exist: create newnode
            print("node not found")
            if self.find(link, None) is not None:                       # check for linked node
                LinkNode = self.find(link, None)
                print("link node found")
            else:
                LinkNode = Vertices(link, None, None)
                print("link node not found")

            NewNode = Vertices(value, LinkNode, int(weight))
            self.list.append(int(value))
            self.list.append(int(link))
            self.weight.append(int(weight))


    def verify(self):                                                   # after each deleting: check if all existing node can connect to each other
        Not_Verified = []                                               # a copy of the existing node list

        for value in self.list:                                         # remove duplicate values
            if value not in Not_Verified:
                Not_Verified.append(value)

        for value in Not_Verified:                                      # check for each node: if linked: can find it
            if self.find(value, None) is None:
                return False

        return True


    def minimize(self):                                                 # to find MST
        copy_weight = self.weight[:]                                    # a copy of weight; assume the weight wont's have duplicate values

        while len(copy_weight) != 0:                                    # reduce the max weight first, until there is no unprocessed weight left
            Max_Weight = max(copy_weight)
            node = self.find(None, Max_Weight)

            for link in node.link:
                if int(link[1]) == Max_Weight:
                    backup = (link[0], link[1])                         # make a backup before delete
                    node.link.remove(link)

                    if not self.verify():                               # if node deleted and cause seperate chain/cannot connect to each other:
                        node.link.append([backup[0], backup[1]])        # restore the backup
                    #print(copy_weight, Max_Weight)    # debug code

            for weight in copy_weight:                                  # after the weight is processed: either successful delete or backup restored: delete the copy weight
                if weight == Max_Weight:
                    copy_weight.remove(weight)
                    #print("deleted") # debug code
                #else:
                    #print(weight, Max_Weight, type(weight), type(Max_Weight)) # debug code


    def traverse(self):
        if not self.init:
            print("Empty MST")
        else:
            self.traverse_sub(self.init)

    def traverse_sub(self, node):
        if len(node.link) != 0:
            #print(node.link) # debug code
            for link in node.link:
                print("%s,%s,%s" % (node.value, link[0].value, link[1]))

        if len(node.link) != 0:
            for link in node.link:
                self.traverse_sub(link[0])


# Demo:
# Description:
infoD = []  # two important value collected from description: value of vertices and edges
infoV_E = []    # each vertices' info: 3 value in total; node, linked node, weight

validD = False
while not validD:
    init = input("Please input the description in format:\n[There are # vertices and # edges]\n\nDescription: ")
    infoD = re.findall(r'\d+', init)    # get important info
    if len(infoD) != 2:                 # if info got is not valid
        print("Invalid Vertices and(or) Edged Number")
        print("\n-------------------------------------------------\n")
        continue
    elif infoD[0] >= infoD[1]:          # if edges are smaller than vertices: impossible
        print("Edges must be greater than Vertices")
        print("\n-------------------------------------------------\n")
    else:
        validD = True

mst = MST()

# Vertices and Weight:
print("\n-------------------------------------------------\n")
print("Please input vertices and weight in format:\n[value, linked value, weight]\ne.g.\t1,2,9\n")

for i in range(int(infoD[1])):          # collect correct amount of vertices
    validV_W = False

    while not validV_W:
        tmp = input("Please input vertices #%s:" % (i + 1))
        infoV_E = tmp.split(",", 3)
        if len(infoV_E) != 3:           # missing value: invalid
            print("Invalid Format\n")
            print("\n-------------------------------------------------\n")
        elif (not infoV_E[0].isdigit()) or (not infoV_E[1].isdigit()) or (not infoV_E[2].isdigit()):    # invalid value
            print("Invalid Vertices and(or) Weight Number\n")
            print("\n-------------------------------------------------\n")
        else:
            validV_W = True

    mst.insert(infoV_E[0], infoV_E[1], infoV_E[2])
    #mst.traverse() # debug code

print("\n-------------------------------------------------\n")
mst.minimize()
mst.traverse()
