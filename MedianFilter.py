# implement update to update an array with median of current and past D scans
class MedianFilter:

    # Hold all past arrays in function
    arrayCollection = []

    # Return the median of the all the arrays
    # Works because update slices the arrayCollection passed in and adds
    # the array that was passed in
    # @param arr the single array passed in to do check on
    # @return array of medians
    def filter(self, arr):

        # tempArray holds the array that the median will be tested on
        # medianArray holds final array of all the medians of indexes
        tempArray = []
        medianArray = []

        # Outer for loop iterates through how many elements are in the list
        # Inner for loop iterates through how many arrays there may be
        # then each respective element of all lists is added to tempArray
        for element in range( len(arr[-1]) ): # get length of last array
            for list in range( len(arr) ):
                tempArray.append(arr[list][element])

            # need a sorted list to do the median on
            tempArray.sort()

            #time to do median calculation
            # check if odd or even then do corresponding median calculation
            if(len(tempArray) % 2 == 0):
                # even number add two numbers in middle then divide by 2
                lowerNumber = tempArray[(len(tempArray) / 2) - 1]
                higherNumber = tempArray[(len(tempArray) / 2)]
                median = (lowerNumber + higherNumber) / 2

                medianArray.append(median)

            else:
                # odd number so get number in the middle, append to list
                median = tempArray[len(tempArray) / 2]

                medianArray.append(median)

            tempArray[:] = [] # clear tempArray

        return medianArray

    # return the array with median of its respective indexes
    # @param arr the array to return temporal median array on
    # @param D the amount of past arrays to use, so we slice it
    # @return array of medians from medianFilter
    def update(self, arr, D):

        self.arrayCollection.append(arr)  # add array to history of medianArray

        # error checking incase D scans is greater than the
        # amount of arrays to look at
        if(len(self.arrayCollection) > D):
            # return -D - 1 slice to get last D items and -1 for new arr
            return self.filter(self.arrayCollection[-D - 1:])
        else:
            return self.filter(self.arrayCollection)
