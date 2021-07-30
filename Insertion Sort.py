Input = []

while True:
    tmp = input("Please input the character that need to be sorted or input space to stop:\n")

    if tmp == ' ' or tmp == '': break
    elif tmp.isalpha(): Input.append(tmp)
    else: print("Characters only!")


def Insertion(array):
    """First: compare the first and second one"""
    if array[1] > array[0]:                                                     # if second character is bigger than the first one, switch their posision
        tmp = array[0]
        array[0] = array[1]
        array[1] = tmp

    for i in range(2,len(array)):
        currentsorting_index = i                                                # current sorting character
        previoussorted_index = i-1                                              # previous sorted character

        while previoussorted_index >= 0:                                        # if exist previous sorted character: continue
            if array[currentsorting_index] > array[previoussorted_index]:       # if previous character is bigger
                """Switch current sorting character with the previous one"""
                tmp = array[previoussorted_index]
                array[previoussorted_index] = array[currentsorting_index]
                array[currentsorting_index] = tmp
            """Continue compare with previous character until there is no previous one"""
            currentsorting_index -= 1
            previoussorted_index -= 1
    print(array)

Insertion(Input)