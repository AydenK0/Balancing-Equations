M = [[2, 0, 2, 0], [1, 2, 1, 0]]
test = M.copy()
def main():
    for i in range(len(M)):
        columns_amount = len(M[i])
        row_ammount = len(M)
        leading_num_index, leading_num = find_leading_num(M[i])
        if leading_num == 1:
            print("Figure out")
            continue
        else:
            row_op_one(leading_num, M[i])
        
        for j in range(i, len(M)):
            if j == i:
                continue
            test[j] = row_op_two(M[i], M[j], leading_num_index)
            print(test)
            



def find_leading_num(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i, row[i]
        
# Multiplies a row by 1/n where n is the value of the leading num
def row_op_one(n, row_matrix):
    mult = 1/n
    temp_matrix = row_matrix.copy()
    for i in range(len(row_matrix)):
        temp_matrix[i] *= mult
    print(temp_matrix)
    pass

# subtracts a row by num such that the num under the leading 1 is 0
def row_op_two(main_row, changing_row, index):
    num = changing_row[index]
    
    if num == 0:
        return changing_row
    for i in range(len(changing_row)):
        changing_row[i] -= num * main_row[i]


main()