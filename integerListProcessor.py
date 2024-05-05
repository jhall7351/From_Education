# FILE: lab8.py
# J Hall, Transy U
# CS 1124, Fall 2020 Module 3
#
#       Read a list of integers that are less than 100. Find the number,
#       totals and averages of non-negative integers, negative integers,
#                      and total integers (separately).
#


def main():

    # title
    print()
    print("INTEGER LIST PROCESSOR")
    print()

    #initialize counters and running totals
    nonNegativeCount = 0
    negativeCount = 0
    nonNegativeTotal = 0
    negativeTotal = 0

    # prompt for and read a list of nonzero integers
    number = eval(input("Enter an integer [>=100 to quit]: "))
    while number < 100:

        # count and add the negative integers
        if number < 0:
            negativeCount = negativeCount + 1
            negativeTotal = negativeTotal + number

        # count and add the non-negative integers
        else:
            nonNegativeCount = nonNegativeCount + 1
            nonNegativeTotal = nonNegativeTotal + number

        # request next digit
        number = eval(input("Enter another integer [>=100 to quit]: "))

    # find the number of total integers
    integersCount = negativeCount + nonNegativeCount

    # find the sum of all the integers
    integersTotal = negativeTotal + nonNegativeTotal

    # find the average of all the integers
    if integersCount > 0:
        integersAverage = integersTotal / integersCount
    else:
        integersAverage = 0.0

    # find the average of non-negative integers
    if nonNegativeCount > 0:
        nonNegativeAverage = nonNegativeTotal / nonNegativeCount
    else:
        nonNegativeAverage = 0.0

    # find the average of the negative integers
    if negativeCount > 0:
        negativeAverage = negativeTotal / negativeCount
    else:
        negativeAverage = 0.0

    ### DISPLAY THE RESULTS
    # integer counts
    print()
    print("\t       There was a total of", integersCount, "integers in the list,")
    print("\twith", negativeCount, "negative integer(s), and", nonNegativeCount, "non-negative integer(s).")
    print()
    
    # integer sums
    print("\tThe sum of all the integers is equal to", integersTotal, "with the sum of")
    print("\t      the negative integers being", negativeTotal, "and the sum of")
    print("\t\t    the non-negative integers being", nonNegativeTotal, ".")
    print()
    
    # integer averages
    print("\tThe average of all of the integers is equal to", integersAverage, "while")
    print("\t   the average for the negative integers is", negativeAverage)
    print("\t\t   and the non-negative average is", nonNegativeAverage, ".")
    print()

    # message to Dr. England
    print()
    print("\t\t Have a good Thanksgiving Dr. England!")
    print()

main()
        
