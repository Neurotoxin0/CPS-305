Input = []

while True:
    tmp = input("Please input the character that need to be sorted or input space to stop:\n")

    if tmp == ' ' or tmp == '': break
    elif tmp.isalpha(): Input.append(tmp)
    else: print("Characters only!")


def Bubble(array):
    Finished = False                          

    while not Finished:
        Finished = True                       

        for i in range(len(array) - 1):                
            if array[i+1] > array[i]:       
                """Switch current sorting character with the next one"""
                tmp = array[i]              
                array[i] = array[i+1]      
                array[i+1] = tmp            
                Finished = False             
            else: continue

    print(array)

Bubble(Input)