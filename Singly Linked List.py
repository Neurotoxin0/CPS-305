import queue

class SinglyLinkedList(object):
    def __init__(self, init_data):              # create an list use data given "init_data"
        self.data = init_data                   # node list
        self.next = None                        # pointer to the next node

    def get(self):                              # get function used to get node
        return self.data

    def get_next(self):                         # get_next function used to get the next node
        return self.next

    def set(self, new_data):                    # set function used to set new node
        self.data = new_data

    def set_next(self, new_data):               # set_next function used to set the pointer to the next node
        self.next = new_data


    def append(self,item):                      # add function used to add node to the end
        tmp = SinglyLinkedList(item)
        current = self.head

        while current.get_next() is not None:   # while still have next node
            current = current.get_next()

        if current is None:                     # if no next node
            self.head = tmp                     # update head pointer

        current.set_next(tmp)                   # point the last pointer to the new added node


    def remove(self, item):                     # remove function used to remove specific node
        current = self.head
        previous = None
        found = False

        while not found:                        # go through the node list
            if current.get() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            if previous is None:                # if is processing the first node
                self.head = current.get_next()  # set pointer to the second node
        else:
            previous.set_next(current.get_next())   # update pointer


    def search(self, item):                     # go through the node list to find specific item
        current = self.head
        index = 0                               # position of the node that is being searched
        while current is not None:
            if current.get() == item:
                print("Position of this element: " + str(index))
                return True
            current = current.get_next()
            index += 1
        return False                            # not found


    def reverse(self):                          # used to reverse the list
        ''''Reverse the list by putting all nodes into another stack(LIFO), and empty the list;
            after the list is empty, use the feature of LIFO-stack to reverse the nodes and put them back one a time
        '''
        tmp = queue.LifoQueue()
        current = self.head

        while current is not None:              # still have next node
            tmp.put(current.get())              # put node into stack
            current = current.get_next()
            self.remove(0)                      # remove the added node
        '''Start to put nodes back'''
        while not tmp.empty():
            self.append(tmp.get())


# Demo:
link_list = SinglyLinkedList(init_data)
#1. delete first node:
link_list.remove(0)
#2. insert to the end：
link_list.append(10)
#3. delete specific node (Ex: 5):
link_list.remove(5)
#4. search specific item (Ex: 6):
link_list.search(6)
#5. reverse the list
link_list.reverse()