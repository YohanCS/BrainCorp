# Import so we can use the classes
from RangeFilter import RangeFilter
from MedianFilter import MedianFilter

#going to be used to store the previous arrays that were passed in
testArrays = [ [0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.],
                [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
                [10., 2., 4., 0., 0.] ]

# Test function
# Will create arrays and call rangeFilter to test rangeFilter
# Will also test medianFilter to test temporal median filter
def test():

    # Create range and median objects to utilize
    range = RangeFilter()
    median = MedianFilter()

    # tests arrays
    testArray1 = testArrays[0][:] #copy of array instead of pointing to it
    testArray2 = [0.02, 0.03, 0.25, 0., 10.]
    testArray3 = [0.2, 0.3, 40., 100., 29.]
    testArray4 = [49., 50., 51., 52., 53.]

    # RangeFilter tests
    print "Array 1 before range filter: ",
    print testArray1
    print "Array 1 after range filter: ",
    print range.update(testArray1)
    print ""


    print "Array 2 before range filter: ",
    print testArray2
    print "Array 2 after range filter: ",
    print range.update(testArray2)
    print ""


    print "Array 3 before range filter: ",
    print testArray3
    print "Array 3 after range filter: ",
    print range.update(testArray3)
    print ""


    print "Array 4 before range filter: ",
    print testArray4
    print "Array 4 after range filter: ",
    print range.update(testArray4)
    print ""

    # calling methods of objects and testing
    #testArray1 = range.update(testArray1)
    #print testArray1
    #testArray1 = testArrays[0][:]

    # Temporal Median Filter tests
    # tests arrays
    testArray1 = testArrays[0][:] #copy of array instead of pointing to it
    testArray2 = testArrays[1][:]
    testArray3 = testArrays[2][:]
    testArray4 = testArrays[3][:]
    testArray5 = testArrays[4][:]

    time = 0
    D = 3
    print "D = " + str(D)  + ", Time = " + str(time) +  "\nArray 1 before median filter: ",
    print testArray1
    print "Array 1 after median filter: ",
    print median.update(testArray1, 3)
    print ""
    time = time + 1

    print "D = " + str(D)  + ", Time = " + str(time) +  "\nArray 2 before median filter: ",
    print testArray2
    print "Array 2 after median filter: ",
    print median.update(testArray2, 3)
    print ""
    time = time + 1

    print "D = " + str(D)  + ", Time = " + str(time) +  "\nArray 3 before median filter: ",
    print testArray3
    print "Array 3 after median filter: ",
    print median.update(testArray3, 3)
    print ""
    time = time + 1

    print "D = " + str(D)  + ", Time = " + str(time) +  "\nArray 4 before median filter: ",
    print testArray4
    print "Array 4 after median filter: ",
    print median.update(testArray4, 3)
    print ""
    time = time + 1

    print "D = " + str(D)  + ", Time = " + str(time) +  "\nArray 5 before median filter: ",
    print testArray5
    print "Array 5 after median filter: ",
    print median.update(testArray5, 3)
    print ""
    time = time + 1




#run test function
if __name__ == "__main__":
    test();
