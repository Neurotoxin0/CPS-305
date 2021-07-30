class Linear_Probing(object):
    def __init__(self, size):
        self.size = size
        self.table = [ '%' for i in range(self.size)]                               # create a array that contain 11 slot (fill with '%')
                                                                                    # use '%' to represent this solot is empty
    def insert(self, value):
        if self.search(value):
            print("--------------------------------------------------")
            index1 = (3 * value + 5) % 11                                           # use given function1 to caculate the index
            probe = 1

            if self.table[index1] == '%':                                           # if index1 is empty: direct insert
                index = index1
                print("Caculated Index(Fun1 Only) for Value %d is: %d, Probe: %d" % (value, index, probe))
            else:                                                                   # is not empty: use function2 to get a index2
                index2 = 7 - (value % 7)
                finish = False

                print("Collision Index(Fun1 Only): %d, Probe: %d" % (index1, probe))

                while not finish:                                                   # use index1, index2 and equation in class to caculate final index
                    index = (index1 + index2 * probe) % self.size                   # keep adding probe by 1 and trying until not collision
                    probe += 1

                    if self.table[index] == '%':                                    # if empty slot: insert
                        finish = True
                        print("\nCaculated Index(Fun 1 & Fun2) for Value %d is: %d, Probe: %d" % (value, index, probe))
                    else:
                        # if not empty: re-run equation
                        print("Collision Index(Fun1 & Fun2): %d, Probe: %d" % (index,probe))


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