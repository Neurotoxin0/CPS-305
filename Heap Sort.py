''' NOT FULLY FUNCTIONING'''

Input = []
Heap = []                                                                   # make and empty array to make heap tree

while True:                                                                 # input module
    tmp = input("Please input the character that need to be sorted or input space to stop")

    if tmp == ' ' or tmp == '':
        Input.sort()                                                        # sort the array first
        break

    elif tmp.isalpha():
        Input.append(tmp)

    else:
        print("Characters only!")


'''Start to build heap tree by appending one value,from 'Input' into 'Heap' each time'''
def HeapBuild():                                                            # descending manner: min heap
    currentIndex = len(Heap) -1                                             # always the last value of the array
    stop = False

    while not stop:                                                         # if already is root value, not need to sort
        '''Get the sorting value's index, floor and position'''
        parentIndex = (currentIndex+1) // 2 - 1

        '''Compare with its parent'''
        if Heap[currentIndex] < Heap[parentIndex]:                          # if current is smaller than its parent, switch them
            #print(currentIndex,Heap[currentIndex],parentIndex,Heap[parentIndex])
            tmp = Heap[parentIndex]
            Heap[parentIndex] = Heap[currentIndex]
            Heap[currentIndex] = tmp
            currentIndex = parentIndex
        else:
            stop = True                                                     # if current is bigger/equal to its parent, break


def HeapSort():
    Len = len(Heap)                                                         # length of the current undeleted heap tree

    while Len > 1:
        currentIndex = 0                                                    # can only delete the root value, which its index is zero
        childIndex = (currentIndex + 1) * 2 - 1                             # the left child

        '''Delete the root value:'''
        '''Ideal process: remove the root value, use the last value to replace root, remove the last value, append the original root value and mark it as deleted '''
        '''Shorter process: switch the root value with the last value, mark the new last value as deleted'''
        tmp = Heap[0]
        Heap[0] = Heap[Len - 1]                                             # replace the root with the last value in the tree
        Heap[Len - 1] = tmp                                                 # store the deleted value to the end of the tree and mark it as deleted
        Len -= 1                                                            # deleted one value: reduce the length of the tree by one to mark

        while childIndex <= Len - 1:
            '''First find the smaller value in next floor'''
            HaveBothSide = False                                            # have right child or not
            Smaller = 0                                                     # 0 = the left child value is smaller; 1 = the right is smaller

            if childIndex + 1 <= Len -1:    HaveBothSide = True
            if HaveBothSide and (Heap[childIndex+1] < Heap[childIndex]):    # if have both children and the right one is smaller
                Smaller = 1

            '''If root value is bigger than its child, switch them'''
            if Heap[currentIndex] > Heap[childIndex+Smaller]:               # if smaller = 0, = left child; if smaller = 1, = left child + 1 = right child
                    tmp = Heap[currentIndex]
                    Heap[currentIndex] = Heap[childIndex+Smaller]
                    Heap[childIndex+Smaller] = tmp
                    currentIndex = childIndex+Smaller                       # the original value has switched with its original child
                    childIndex = (currentIndex + 1) * 2 - 1

            else: break                                                     # if current value is already smaller than its childen/child, break

    print(Heap)                                                             # if only the root value is not deleted: finish sorting


for character in Input:                                                     # adding one value a time to heap tree and build it
    Heap.append(character)
    HeapBuild()
#print(Heap)
#print("-----------------------------------")
'''Finish build heap tree'''

HeapSort()                                                                  # start sorting