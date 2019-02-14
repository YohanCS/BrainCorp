# constants for range min and range max of values
range_min = 0.3
range_max = 50.0

#used to print debug statements
debug = False

#going to be used to store the previous arrays that were passed in
medianArray = [ [0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.],
                [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.],
                [10., 2., 4., 0., 0.] ]

# Test function
# Will create arrays and call rangeFilter to test rangeFilter
# Will also test medianFilter to test temporal median filter
def test():
    name = raw_input("Type 'x' for debug mode: ")
    if(name is 'x'):
        global debug #modify global debug to be true
        debug = True
    testArray1 = medianArray[0]
    testArray2 = medianArray[1]
    testArray3 = medianArray[2]
    testArray4 = medianArray[3]
    testArray5 = medianArray[4]
    rangeFilter(testArray1)

# Crops all values below range_min (resp above range_max)
# and replaces them with the range_min value (resp above range max)
# @param arr the single array passed in to do check on
def rangeFilter(arr):
    #simple for loop through the array in log(n) time
    #modifies array[index] to range_min or range_max if out of range
    if(debug):
        print "[Array before rangeFilter: " + arr + "]"
    for index in range(len(arr)):
        if(arr[index] < range_min ):
            arr[index] = range_min
        elif(arr[index] > range_max):
            arr[index] = range_max
    if(debug == 1):
        print "Array after rangeFilter: " + arr + "]"

    return arr

# Return the median of the current and previous arrays
# @param arr the single array passed in to do check on
# @param D the number of previous scans to look at using medianArray
def medianFilter(arr, D):
    print "nothing yet"
    #for loop


#run test function
if __name__ == "__main__":
    test();
