import re

Vector = []
'''Get the total number of vectors'''
total = input("Please input the number of vectors: ")
while not total.isdigit():
    print("Integer Only!")
    total = input("Please input the number of vectors: ")

print("Number of vectors: " + str(total) + "\n\nPlease input vectors: each vector per line, split with space")
'''Start to get vectors'''
for i in range(int(total)):
    vector_tmp = input("Please input vector " + str(i+1) + ": ")
    vector_tmp = re.sub("\D", "", vector_tmp)
    Vector.append(int(vector_tmp))


def RadixSort(vectors):
    Max_Bit = len(str(max(vectors)))                                                # the highest bit among given vectors (10**10 in this case)

    for bit in range(Max_Bit):                                                      # how many round should it operate
        count_array = [[] for i in range (10)]                                      # create ten empty arrays to stand [0 - 9]
        current_process_bit = 10**bit                                               # current processing bit (1, 10, 100, 1000, etc.)

        """
            What supposed to do: count each vectors' processing bit and add one to count_array each time; 
            use count_array to get index for where each vector should be put;
            put each vector back from end to begin, according to the calculated index 
        
            Simplified: store each vector itself to those ten count_array according to its processing bit;
            Take vector out from count_array[0] to count_array[9]; 
            for it was taken out in ascending order (from 0 to 9), therefore it is sorted
        """
        for vector in vectors:
            count_array[(vector // current_process_bit) % 10].append(vector)       # (vector // current_process_bit) = find the processing bit, make sure it's right before the decimal and clear digits afrer decimal
                                                                                   # ([caculated above] % 10) = put the processing bit after decimal and use '%' to get the processing bit; append it to the right count_array
        vectors = [j for i in count_array for j in i]                              # put vectors back to array 'vectors' by accessing each elements in count_array from [0] to [9]

    return vectors


Vector = RadixSort(Vector)

for vector in Vector:
    output = ""
    for digit in str(vector):
        output += digit + ';'
    print(output)
