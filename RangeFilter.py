# constants for range min and range max of values
range_min = 0.3
range_max = 50.0

# Implement update of an array and filter range values of an array
class RangeFilter:

    # Crops all values below range_min (resp above range_max)
    # and replaces them with the range_min value (resp above range max)
    # @param arr the single array passed in to do check on
    def filter(self, arr):
        #simple for loop through the array in log(n) time
        #modifies array[index] to range_min or range_max if out of range
        for index in range(len(arr)):
            if(arr[index] < range_min ):
                arr[index] = range_min
            elif(arr[index] > range_max):
                arr[index] = range_max

        return arr

    # Calls on filter to filter the ranges in the N-length array
    # Then returns the filtered length N array
    def update(self, arr):
        return self.filter(arr)
