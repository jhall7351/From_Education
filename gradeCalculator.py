# FILE: p2.py
# J Hall, Transy U
# CS 1124, Fall 2020, Module 3
#
#       Calculate and provide a summary of a students total grade
#                    for a computer science course.
#

def main():

    # title
    print()
    print("\t\t     COMPUTER CLASS GRADE CALCULATOR")
    print()

    # initialize counters and running totals
    projectCount = 0
    projectTotal = 0
    gradeAProjects = 0
    testCount = 0
    testTotal = 0

    # prompt for and read a list of project grades
    projectGrade = eval(input("Enter your first project grade [negative value to quit]: "))
    while projectGrade >= 0:

        # count and add the project grades
        projectCount = projectCount + 1
        projectTotal = projectTotal + projectGrade

        # count the number of grade A projects
        if projectGrade >= 90.0:
            gradeAProjects = gradeAProjects + 1

        # request next project grade
        projectGrade = eval(input("Enter your next project grade [negative to quit]: "))

    # calculate project average
    if projectCount > 0:
        projectAverage = projectTotal / projectCount

    # convert project average to final grade percentage
    projectPercentGrade = projectAverage * .40

    # prompt for and read the lab average
    print()
    labAverage = eval(input("Enter your lab grade average: "))

    # convert lab average to final grade percentage
    labPercentGrade = labAverage * .10

    # prompt for and read the test 1 grade
    print()
    test1Grade = eval(input("Enter your Test 1 grade: "))
    testCount = testCount + 1
    testTotal = testTotal + test1Grade

    # convert test 1 grade to final grade percentage
    test1PercentGrade = test1Grade * .15

    # prompt for and read the test 2 grade 
    test2Grade = eval(input("Enter your Test 2 grade: "))
    testCount = testCount + 1
    testTotal = testTotal + test2Grade

     # convert test 2 grade to final grade percentage
    test2PercentGrade = test2Grade * .15

    # calculate test average
    if testCount > 0:
        testAverage = testTotal / testCount

    # prompt for and read the final exam grade
    print()
    finalExamGrade = eval(input("Enter your Final Exam grade: "))

    # convert final exam grade to final grade percentage
    examPercentGrade = finalExamGrade * .20

    # cumulative course grade
    courseGrade = projectPercentGrade + labPercentGrade + test1PercentGrade + test2PercentGrade + examPercentGrade
    

    ### DISPLAY THE RESULTS
    print()
    print("\t\t           GRADE REPORT")
    # number of projects, project average and number of grade A projects
    print()
    print("\t      The average of your", projectCount, "projects is", projectAverage, "%,")
    print("\t\t            with", gradeAProjects, "A('s).")

    # lab grade
    print()
    print("\t           You scored a Lab Grade of", labAverage, "%.")
    print()

    # test average
    print()
    print("\t          You have a Test Average of", testAverage, "%.")
    print()

    # final exam
    print()
    print("\t     And you earned a(n)", finalExamGrade, "% on the Final Exam,")
    print()

    # cumulative course grade
    print()
    print("\t       for a cumulative course grade of", courseGrade, "%.")
    print()

    # passed the class?
    if courseGrade <= 59.99:
        print()
        print("   Uh oh, unfortunately you have failed the course this time around.")
        print("\t        Best of luck if you choose to try again!")

    if 60.0 <= courseGrade <= 89.99:
        print()
        print("\t        Good work, you've passed this course!")
        print()

    if courseGrade >= 90.0:
        print()
        print("\t  Incredible job, you've passed this course with an A!")
        print()
                     
main()
                     
                     
        
                 
