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
    testArray2 = testArrays[1]
    testArray3 = testArrays[2]
    testArray4 = testArrays[3]
    testArray5 = testArrays[4]


    # calling methods of objects and testing
    #testArray1 = range.update(testArray1)
    #print testArray1
    #testArray1 = testArrays[0][:]

    testArray1 = median.update(testArray1, 3)
    testArray2 = median.update(testArray2, 3)
    testArray3 = median.update(testArray3, 3)
    testArray4 = median.update(testArray4, 3)
    testArray5 = median.update(testArray5, 3)
    print "Array 1 : ",
    print(testArray1)
    print "Array 2 : ",
    print(testArray2)
    print "Array 3 : ",
    print(testArray3)
    print "Array 4 : ",
    print(testArray4)
    print "Array 5 : ",
    print(testArray5)



#run test function
if __name__ == "__main__":
    test();
