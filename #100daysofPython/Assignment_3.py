def tests(test1, test2):
    # This function takes in two test marks and returns the higher one.
    if test1 == test2:
        # If the two marks are the same, it returns either one.
        return test1
    else:
        # Otherwise, it returns the higher mark.
        return test2

#Running the tests   
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))


def courseWrk(cswork):
    # This function takes in the coursework mark and calculates the final coursework marks.
    testsMark = tests(test1,test2)
    # It calls the tests function to get the higher of the two test marks.
    avgtestsCswork = (cswork + testsMark)/2
    # It calculates the average of the coursework and tests marks.
    fnltestsCswork = avgtestsCswork * (40/100)
    # It calculates the final coursework marks by multiplying the average by 40%.
    print('..............................')
    # Prints a line of dots for formatting purposes.
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
    # Prints the final coursework marks with some more formatting.

#prompting the user to enter course work marks
cswork = int(input('Please enter your course work Marks: '))
#calling the function
courseWrk(cswork)



