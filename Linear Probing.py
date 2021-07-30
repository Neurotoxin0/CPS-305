class Linear_Probing(object):
    def __init__(self, size):
        self.size = size
        self.table = [ '%' for i in range(self.size)]                               # create a array that contain 11 slot (fill with '%')
                                                                                    # use '%' to represent this solot is empty
    def insert(self, value):
        if self.search(value):
            print("--------------------------------------------------")
            index = (3 * value + 5) % 11                                            # use given function to caculate the index
            probe = 1

            while self.table[index] != '%':                                         # if not empty: collision: go try next index (+1)
                print("Collision Index: %d, Probe: %d" % (index,probe))
                probe += 1
                index += 1
                if index == self.size-1:                                            # if reach end of table, go bakc to index[0]
                    index = 0

            print("\nCaculated Index for Value %d is: %d, Probe: %d" % (value, index,probe))
            self.table[index] = value
            self.traverse()
        else:
            print("Value already in Table")

    def search(self, value):                                                        # not in requirement: avoid same value in one table occur twice
        for node in self.table:
            if value == node:
                return False
        return True

    def traverse(self):
        print("Table in Python: ")
        print(self.table)
        print("Value Only: ")
        for a in self.table:
            if a != '%':
                print(a, end = ",")
        print('\n')


# Demo:
test = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
hashlist = Linear_Probing(len(test))

for i in test:
    hashlist.insert(i)