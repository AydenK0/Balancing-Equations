import numpy as np
from sympy import *
import math

test_var = {"test1":{"elements" : ["H", "O"], "formula" : "H2 + O2 -> H2O"},
            "test2":{"elements" : ["H", "Cl", "C"], "formula": "CH4 + Cl2 -> CCl4 + HCl"},
            "test3":{"elements" : ["C","H","O"], "formula": "CO2 + H2O -> C6H12O6 + O2"},
            "test4":{"elements" : ["Si","Cl","H","O"], "formula": "SiCl4 + H2O -> H4SiO4 + HCl"},
            "test5":{"elements" : ["Fe","S","O","K","H"], "formula": " Fe2(SO4)3 + KOH -> K2SO4 + Fe(OH)3"},
            "test6":{"elements" : ["Ca","P","O","Si"], "formula": "Ca3(PO4)2 + SiO2 -> P4O10 + CaSiO3"},
            "test7":{"elements" : ["H", "S", "I", "O"], "formula": "H2SO4 + HI -> H2S + I2 + H2O"},
            "blank":{"elements" : [], "formula": ""},}

def main():
    matrix, elements, formula, ident = user_input()
    reduced_matrix = row_reduce(matrix)
    print("Reduced Matrix", reduced_matrix)
    co_efficents = find_coeff(reduced_matrix)
    print("Coefficients", co_efficents)
    final_coeff = calc_final_coeff(co_efficents)
    display_results(final_coeff, elements, formula, ident)


    

def user_input():
    elements = []
    formula = ""
    temp_list = []
    ident = ["+", "->", "=", ">"]
    while True:
        print("Enter each element in one by one until all elements have been inputted. (Be specific with capitalization Co -> Cobalt, C -> Carbon O -> Oxygen)")
        print("Type 'quit' to move on")
        print("")
        element = input("Enter an element in the equation: ")
        print("")
        if element == "quit":
            break
        elif element in test_var:
            print(test_var[element])
            elements = test_var[element]["elements"]
            formula = test_var[element]["formula"]
            break
        else:
            elements.append(element)
            formula = input("Please enter full chemical equation (use either = or -> to separate inputs and outputs)")

    mold = [0]
    count = 1
    for i in formula:
        if i in ident:
            count += 1
    mold = mold * count
    mold.append(0)
    #print(mold)

    

    for ele in elements:
        spot_in_mold = 0
        count_ele = mold.copy()
        multiple = 1
        #print("Print 1:", count_ele)
        for i in range(len(formula)):
            was_int = False
            #print(count_ele)
            if formula[i] in ident:
                spot_in_mold += 1

            if formula[i] == "(":
                k = 1
                str_multiple = ""
                location = (formula.find(")", i, len(formula)-1))

                
                while True:
                    
                    if location+k <= len(formula)-1 and (formula[location + k]).isdigit():
                        str_multiple += str(formula[location+k])
                        k += 1
                    else:
                        break
                multiple = int(str_multiple)

            if formula[i] == ")":
                multiple = 1

            if formula[i] == ele:
                try:
                    if formula[i+1] is None:
                        print("Nope not there")
                except:
                    #count_ele.append(1)
                    count_ele[spot_in_mold] = 1 * multiple
                    #print("Found Void, Single: " + ele)
                    #spot_in_mold += 1
                    continue

                if formula[i+1] == " " or formula[i+1] == "+"  or formula[i+1] == "(" or formula[i+1] == ")" or formula[i+1].isupper():
                    #count_ele.append(1)
                    count_ele[spot_in_mold] = 1 * multiple
                    #print("Found Space/+, Single: " + ele)
                    #spot_in_mold += 1

                try:
                    n = 1
                    while True:
                        int(formula[i+n])
                        was_int = True
                        #count_ele.append(formula[i+2])
                        if count_ele[spot_in_mold] == 0:
                            count_ele[spot_in_mold] = formula[i+n]
                        else:
                            count_ele[spot_in_mold] += formula[i+n]
                        n += 1
                    #print("Found Int, Single: " + ele)
                    #spot_in_mold += 1
                except:
                    if was_int == True:
                        count_ele[spot_in_mold] = str(int(count_ele[spot_in_mold]) * multiple)
                    #print(formula[i+1], "not an int")
                    pass
                
            if len(ele) == 2 and formula[i] == ele[0]:
                try:
                    if formula[i+1] == ele[1]:
                        try:
                            if formula[i+2] is None:
                                print("Nope not there")
                        except:
                            #count_ele.append(1)
                            count_ele[spot_in_mold] = 1 * multiple
                            #print("Found Void, Double: " + ele)
                            #spot_in_mold += 1
                            continue
        
                        if formula[i+2] == " " or formula[i+2] == "+" or formula[i+2] == "(" or formula[i+2] == ")" or formula[i+2].isupper():
                            #count_ele.append(1)
                            count_ele[spot_in_mold] = 1 * multiple
                            #print("Found Space/+, Double: " + ele)
                            #spot_in_mold += 1
                        try:
                            n = 2
                            while True:
                                int(formula[i+n])
                                was_int = True
                                #count_ele.append(formula[i+2])
                                if count_ele[spot_in_mold] == 0:
                                    count_ele[spot_in_mold] = formula[i+n]
                                else:
                                    count_ele[spot_in_mold] += formula[i+n]
                                n += 1
                                #print("Found Int, Double: " + ele)
                                #spot_in_mold += 1
                        except:
                            if was_int == True:
                                count_ele[spot_in_mold] = str(int(count_ele[spot_in_mold]) * multiple)
                            #print(formula[i+2], "not an int")
                            pass
                except:
                    continue

        temp_list.append(count_ele)
    print(temp_list)

    
    
    M = Matrix(temp_list)
    print(M)

    return M, elements, formula, ident


def row_reduce(M):
    RREF = M.rref(M)
    RREF = RREF[0].tolist()
    return RREF

def find_coeff(RREF):
    coeff = []

    for i in range(len(RREF)):
        for j in range(len(RREF[i])-1, 0, -1):
            if RREF[i][j] != 0:
                coeff.append(RREF[i][j])
                break

    coeff.append(1)

    return(coeff)

        
def calc_final_coeff(coeff):
    mult = LCD(coeff)
    for i in range(len(coeff)):
        coeff[i] = abs(coeff[i]) * mult
    return coeff

def LCD(nums):
    denom = [num.denominator for num in nums]
    lowest_com_den = denom[0]
    for d in denom[1:]:
        #print(lowest_com_den)
        #print(d)
        lowest_com_den = lcm(lowest_com_den, d) 
    return lowest_com_den

def display_results(coeff, elements, formula, ident):
    count = 1
    new_formula = str(coeff[0]) + formula
    for i in range(len(new_formula)):
        if new_formula[i] in ident:
            if new_formula[i+1] == " ":
                new_formula = new_formula[:i+1] + " " + str(coeff[count]) + new_formula[i+2:]
            else:
                new_formula = new_formula[:i+1] + " " + str(coeff[count]) + new_formula[i+1:]
            count += 1
    print("Balanced Equations")
    print("-------------------")
    print(new_formula)


main()

