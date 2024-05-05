# FILE: examGrades.py
# J Hall, Transy U
# CS 1124, Fall 2020, Module 3
#
#               Design a program that requests, passes/fails,
#                         and averages 5 test grades.
#

def main():
    # set running totals
    testCount = 0
    testTotal = 0
    testPass = 0

    # request only 5 test grades
    for i in [1,2,3,4,5]:
        test = eval(input("Test Grade: "))
        testCount = testCount + 1
        testTotal = testTotal + test
        if test >= 60.0:
            print("Passing Grade")
            print()
            testPass = testPass + 1
        else:
            print("Failing Grade")
            print()

    # find average of all tests
    testAverage = testTotal / testCount

    ### display results
    # passing test grades
    print("\tWith", testPass, "passing grades, the student")

    # all test average
    print("\tscored a test average of", testAverage, ".")
    
            

main()
