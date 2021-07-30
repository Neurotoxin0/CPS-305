class Separate_Chaining(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(self.size)]                                 # create a big array that contain 11(same as size) empty array

    def insert(self, value):
        if self.search(value):
            index = (3 * value + 5) % 11
            print("--------------------------------------------------")
            print("Caculated Index for Value %d is: %d" %(value,index))
            self.table[index].append(value)
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
            for b in a:
                print(b, end = ",")
        print('\n')


# Demo:
test = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
hashlist = Separate_Chaining(len(test))

for i in test:
    hashlist.insert(i)