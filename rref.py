def RREF(matrix):
    matrix = matrix.copy()
    reduced_matrix = []
    row_reduced_matrix = []

    reduced_matrix = ref(matrix)
    row_reduced_matrix = top_zeros(reduced_matrix)
    sorted_matrix = row_op_three(row_reduced_matrix)
    final_matrix = diag_matrix(sorted_matrix)
    return row_reduced_matrix
            
# Gets a diagonal of 1's and has all values under leading 1's equaling 0
def ref(matrix):
    for i in range(len(matrix)):
        columns_amount = len(matrix[i])
        row_ammount = len(matrix)
        leading_num_index, leading_num = find_leading_num(matrix[i])
        if leading_num_index == -1:
            continue

        if leading_num != 1:
            matrix[i] = row_op_one(leading_num, matrix[i])
        
        for j in range(i, len(matrix)):
            if j == i:
                continue
            matrix[j] = row_op_two(matrix[i], matrix[j], leading_num_index)
            print(matrix)
    return matrix

def top_zeros(matrix):
    for i in range(len(matrix)-1 , -1, -1):
        leading_one_index = find_leading_ones(matrix[i])
        if leading_one_index != -1:
            for j in range(0,i):
                matrix[j] = row_op_two(matrix[i], matrix[j], leading_one_index)
    return matrix


def find_leading_ones(row):
    for i in range(len(row)):
        if row[i] == 1:
            return i
    return -1

def find_leading_num(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i, row[i]
    return -1, -1
        
# Multiplies a row by 1/n where n is the value of the leading num
def row_op_one(n, row_matrix):
    mult = 1/n
    temp_matrix = row_matrix.copy()
    for i in range(len(row_matrix)):
        temp_matrix[i] *= mult
    print(temp_matrix)
    return temp_matrix

# subtracts a row by num such that the num under the leading 1 is 0
def row_op_two(main_row, changing_row, index):

    num = changing_row[index]
    
    if num == 0:
        return changing_row
    for i in range(len(changing_row)):
        changing_row[i] -= num * main_row[i]
    return changing_row

# Checks for a row of zeros, if there is one it moves it to the bottom of the array
def row_op_three(matrix):
    
    for i in range(len(matrix)):
        
        if matrix[i] == ([0] * len(matrix[i])):
            zero_matrx = matrix.pop(i)
            matrix.append(zero_matrx)
            i -= 1
        
    return matrix

def diag_matrix(matrix):
    location = []
    for i in range(len(matrix)):
        index = find_leading_ones(matrix[i])
        if index != -1:
            location.append(index)
    count = 0
    for i in range(len(location)):
        if location[i] == count:
            count += 1
            continue
        
        for j in range(i,len(location)):
            if location[j] == count:
                
                temp_num = 0
                temp_matrix = []

                temp_num = location[i]
                location[i] = location[j]
                location[j] = temp_num

                temp_matrix = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = temp_matrix
                count += 1
    return matrix