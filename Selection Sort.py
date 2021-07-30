Input = []

while True:
    tmp = input("Please input the character that need to be sorted or input space to stop:\n")

    if tmp == ' ' or tmp == '': break
    elif tmp.isalpha(): Input.append(tmp)
    else: print("Characters only!")


def Selection(array):
    for a in range(len(array)):                   
        currentmax = a                              
        for b in range(a+1,len(array)):                    
            if array[b] > array[currentmax]:        
                currentmax = b
            else: continue

        """Change current max character with the current sorting one"""
        tmp = array[a]
        array[a] = array[currentmax]
        array[currentmax] = tmp

    print(array)

Selection(Input)