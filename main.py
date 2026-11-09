import numpy as np
from sympy import *
import math
import json
from fractions import Fraction
from rref import RREF
# All code was made by Ayden Knowles using no AI
# Some of the math used to solve the unbalence equations was helped by Daniel Shelton

'''
TODO: 
Console based program:
X - Add error handling for user input 
X - Add a check for if the chemical equation is possible: Check if both sides have the same elements
X - Shorten creation of matrix 
X - Create code that does RREF without imports
Make LCM function to replace imported lcm function 
X - Fix paratneses before plus bug
------------
Add a GUI:

Add a periodic table with buttons to select an element
'''

seperators = ["->", "=", ">", "→"]


# Controls the flow of the program. Console based
def console_main():
    while True:
        formula, ident = user_input()
        
    
        if check_valid_eqn(formula,ident) == True:
            break
        else:
            print("Not a valid chemical formula")
            print("Please enter a valid chemical formula")

            
    elements = find_elements(formula)
    print("Elements", elements)

    mold = create_mold(formula, ident)

    matrix = create_matrix(mold, elements, formula, ident)

    reduced_matrix = row_reduce(matrix)

    print("Reduced Matrix", reduced_matrix)

    co_efficents = find_coeff(reduced_matrix)

    print("Coefficients", co_efficents)

    final_coeff = calc_final_coeff(co_efficents)

    display_results(final_coeff, elements, formula, ident, False)

# Controls the flow of the program.
def app_main(formula):
    while True:
        ident = ["+", "->", "=", ">", "→"]
        
    
        if check_valid_eqn(formula,ident) == True:
            break
        else:
            print("Not a valid chemical formula")
            print("Please enter a valid chemical formula")
            return

            
    elements = find_elements(formula)
    print("Elements", elements)

    mold = create_mold(formula, ident)

    matrix = create_matrix(mold, elements, formula, ident)

    reduced_matrix = row_reduce(matrix)

    print("Reduced Matrix", reduced_matrix)

    co_efficents = find_coeff(reduced_matrix)

    print("Coefficients", co_efficents)

    final_coeff = calc_final_coeff(co_efficents)

    display_results(final_coeff, elements, formula, ident, False)


# This functions runs tests for all the tests in test.json
# It checks that they are valid equations and checks if the answers are correct
# It will only check answers if it's a valid equation
def run_tests(ident):
    test_results = []
    tests = load_tests()
    score_checks = 0
    max_score_checks = 0

    score_answers = 0
    max_score_answers = 0

    
    for test_xx in tests["tests"]:
        #print(tests["tests"][test_xx])
        test_num = tests["tests"][test_xx]["test_num"]
        unbalenced_equation = tests["tests"][test_xx]["unbalenced"]
        balanced_equation = tests["tests"][test_xx]["balenced"]

        if test_num == "test_XX":
            continue
        
        max_score_checks += 1
        if check_valid_eqn(unbalenced_equation, ident) == True:
            score_checks += 1
            #print(test_num, "Test Completed Succesfully")
            test_results.append(f"{test_num}, Completed Succesfully")

            answer = test_answer(unbalenced_equation, ident)

            max_score_answers += 1
            if answer == balanced_equation:
                score_answers += 1
                test_results.append(f"{test_num}, Matches")
            else:
                test_results.append(f"{test_num}, Does Not Match")
                print(f"Answer: {answer}, Documented Answer: {balanced_equation}")

        else:
            #print(test_num, "Test Failed")
            test_results.append(f"{test_num}, Failed")
           
        

            

    for i in test_results:
        print(i)
    print(f"Score Checks: {score_checks}/{max_score_checks}")
    print(f"Score Answers: {score_answers}/{max_score_answers}")
    return

# This function finds the answers using the program and returns it
def test_answer(formula, ident):
    elements = find_elements(formula)

    mold = create_mold(formula, ident)

    matrix = create_matrix(mold, elements, formula, ident)

    reduced_matrix = row_reduce(matrix)

    co_efficents = find_coeff(reduced_matrix)

    final_coeff = calc_final_coeff(co_efficents)

    answer = display_results(final_coeff, elements, formula, ident, True)

    return answer

# Loads the test from a JSON file
def load_tests():
    try:
        with open("test.json") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error Loading data; {e}")
        return {}


# Gets the user input for elements and the formula.
# Returns a list of elements, the formula, and a list of identifiers.
def user_input():
    elements = []
    formula = ""
    ident = ["+", "->", "=", ">", "→"]
    while True:
        formula = input("Please enter full chemical equation (use either = or -> to separate inputs and outputs)")
        print("")
        
        if formula == "quit":
            break

        if formula == "test_all":
            run_tests(ident)
            quit()
        break
    print(formula)
    return formula, ident

# Creates a mold for the matrix and augmments it with 0
# Returns a list of 0's with the length of the number of elements in the formula.
def create_mold(formula, ident):
    mold = [0]
    count = 1
    for i in formula:
        if i in ident:
            count += 1
    mold = mold * count
    mold.append(0)
    return mold
    #print(mold)

# Checks if the equation is a valid equation using the built in checks
def check_valid_eqn(formula,ident):
    
    check1 = check_one(formula)
    check2 = check_two(formula,ident)
    check3 = check_three(formula)
    check4 = check_four(formula)
    check5 = check_five(formula)

    checks = [check1, check2, check3, check4, check5]

    if False in checks:
        print(checks)
        return False
    else:
        return True

# Checks if there are the same elements on both sides
def check_one(formula):
    elements_left = []
    middle = 0
    elements_right = []
    for i in range(len(formula)):
        if formula[i].isupper():
            if i+1 <= len(formula)-1 and formula[i+1].islower():
                if (formula[i] + formula[i+1]) not in elements_left:
                    elements_left.append(formula[i] + formula[i+1])
            else:
                if formula[i] not in elements_left:
                    elements_left.append(formula[i])
        if formula[i] in seperators:
            middle = i
            break
    for i in range(middle, len(formula)):
        if formula[i].isupper():
            if i+1 <= len(formula)-1 and formula[i+1].islower():
                if (formula[i] + formula[i+1]) not in elements_right:
                    elements_right.append(formula[i] + formula[i+1])
            else:
                if formula[i] not in elements_right:
                    elements_right.append(formula[i])
    if sorted(elements_left) != sorted(elements_right):
        return False
    if elements_left == []:
        print("No elements")
        return False
    return True

# Checks for incomplete parantheses
def check_two(formula,ident):
    tracker = []
    for char in formula:
        if char == "(":
            tracker.append(char)
        if char == ")" and len(tracker) > 0:
            tracker.pop()
        elif char == ")" and len(tracker) == 0:
            print("Missing a parenthesis")
            return False
        if (char == "+" or char in ident) and len(tracker) != 0:
            return False
    if len(tracker) != 0:
        print("Missing a parenthesis")
        return False
    return True
    

# Checks for non-elements in user-input (checks for impossible elements, aka starts with lowercase or has more than 3 letters)
def check_three(formula):
    for i in range(len(formula)):
        if formula[i].islower():
            if i > 0:
                if formula[i-1].islower():
                    print("Double lower case element, check formula")
                    return False
                
    return True
    

# Checks for invalid/out of place numbers
def check_four(formula):
    for i in range(len(formula)):
        if formula[i].isnumeric():
            for j in range(i,0,-1):
                if not (formula[j].isnumeric() or formula[j].isalpha() or formula[j] == ")"):
                    print("failed")
                    print(formula[j])
                    return False
                if formula[j].isnumeric():
                    continue
                if formula[j].isalpha() or formula[j] == ")":
                    break
            
    return True
    pass

# Checks for both sides of the chemical equation
def check_five(formula):
    for i in seperators:
        print(formula)
        if i in formula:
            return True
    print("Only one side of chemical equation exists")
    return False

# Finds the elements and saves them
# Also checkes if the chemical equation is valid based on if elements are the same on both sides
def find_elements(formula):
    elements = []
    
    for i in range(len(formula)):
        if formula[i].isupper():
            if i+1 <= len(formula)-1 and formula[i+1].islower():
                if (formula[i] + formula[i+1]) not in elements:
                    elements.append(formula[i] + formula[i+1])
            else:
                if formula[i] not in elements:
                    elements.append(formula[i])
        if formula[i] in seperators:
            break
    
    return elements



# Creates a matrix based on the elements and the formula.
# Returns a matrix, the elements, the formula, and the identifiers.
def create_matrix(mold, elements, formula, ident):
    temp_list = []
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
                
                if i+1 >= len(formula):
                    print("Nope not there")
                    count_ele[spot_in_mold] = 1 * multiple
                    continue

                if formula[i+1] == " " or formula[i+1] == "+"  or formula[i+1] == "(" or formula[i+1] == ")" or formula[i+1].isupper():
                    count_ele[spot_in_mold] = 1 * multiple


                n = 1
                while True:
                    if i+n >= len(formula):
                        break
                    if formula[i+n].isdigit():
                        was_int = True
                        #count_ele.append(formula[i+2])
                        if count_ele[spot_in_mold] == 0:
                            count_ele[spot_in_mold] = formula[i+n]
                        else:
                            count_ele[spot_in_mold] += formula[i+n]
                        n += 1
                    else:
                        if was_int == True:
                            count_ele[spot_in_mold] = str(int(count_ele[spot_in_mold]) * multiple)
                        break
  
            if len(ele) == 2 and formula[i] == ele[0]:
                
                if formula[i+1] == ele[1]:
                    if i+2 >= len(formula):
                        print("Nope not there")
                        count_ele[spot_in_mold] = 1 * multiple
                        continue
    
                    if formula[i+2] == " " or formula[i+2] == "+" or formula[i+2] == "(" or formula[i+2] == ")" or formula[i+2].isupper():
                        count_ele[spot_in_mold] = 1 * multiple

                    n = 2
                    while True:
                        if i+n >= len(formula):
                            break
                        if formula[i+n].isdigit():
                            was_int = True
                            #count_ele.append(formula[i+2])
                            if count_ele[spot_in_mold] == 0:
                                count_ele[spot_in_mold] = formula[i+n]
                            else:
                                count_ele[spot_in_mold] += formula[i+n]
                            n += 1
                        else:
                            if was_int == True:
                                count_ele[spot_in_mold] = str(int(count_ele[spot_in_mold]) * multiple)
                            break

        for i in range(len(count_ele)):
            count_ele[i] = int(count_ele[i])
        temp_list.append(count_ele)
    #print(temp_list)

    #M = Matrix(temp_list) -- needed for old RREF
    M = temp_list
    print(M)

    return M


# Uses RREF to row reduce the matrix.
# Returns the row reduced matrix.
def row_reduce(M):
    reduced_matix = RREF(M)
    
    return reduced_matix

# Old RREF just in case
"""
def row_reduce(M):
    RREF = M.rref(M)
    RREF = RREF[0].tolist()
    return RREF
"""


# Finds the coefficients of the elements in the row reduced matrix. 
# Also appends a 1 to the end of the list of coefficients to account for the free variable in the system of equations.
# Returns a list of coefficients.
def find_coeff(RREF):
    coeff = []

    for i in range(len(RREF)):
        for j in range(len(RREF[i])-1, 0, -1):
            if RREF[i][j] != 0:
                coeff.append(RREF[i][j])
                break

    coeff.append(1)

    return(coeff)

# Calculates the final coefficients by finding the least common denominator and multiplying each coefficient by it.
# Returns a list of final coefficients.       
def calc_final_coeff(coeff):
    mult = LCD(coeff)
    print(mult)
    for i in range(len(coeff)):
        dec_coeff = (abs(coeff[i]) * mult)
        
        coeff[i] = int(dec_coeff + 0.5)
    return coeff

# Finds the least common denominator of a list of numbers.
# Returns the least common denominator.
def LCD(nums):
    denom = [Fraction(num).limit_denominator().denominator for num in nums]
    lowest_com_den = denom[0]
    for d in denom[1:]:
        #print(lowest_com_den)
        #print(d)
        lowest_com_den = lcm(lowest_com_den, d) 
    
    return lowest_com_den

# Displays the final results in a balanced equation format if not testing.
# Returns nothing if not testing
# If testing it returns final results instead of printing them
def display_results(coeff, elements, formula, ident, testing):
    count = 1
    if testing:
        for i in range(len(coeff)):
            if coeff[i] == 1:
                coeff[i] = ""

    new_formula = str(coeff[0]) + formula
    for i in range(len(new_formula)):
        if new_formula[i] in ident:
            if new_formula[i+1] == " ":
                new_formula = new_formula[:i+1] + " " + str(coeff[count]) + new_formula[i+2:]
            else:
                new_formula = new_formula[:i+1] + " " + str(coeff[count]) + new_formula[i+1:]
            count += 1

    if not testing:
        print("Balanced Equations")
        print("-------------------")
        print(new_formula)
        return
    return new_formula

# Starts the program by calling the main function.
if __name__ == "__main__":
    main()


