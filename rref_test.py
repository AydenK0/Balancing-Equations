M = [[2, 0, 2, 0], [0, 2, 1, 0]]
test = M.copy()
def main():
    for i in range(len(M)):
        columns_amount = len(M[i])
        row_ammount = len(M)
        leading_num_index, leading_num = find_leading_num(M[i])
        if leading_num == 1:
            print("Figure out")
            continue

        
        


    pass

def find_leading_num(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i, row[i]



main()