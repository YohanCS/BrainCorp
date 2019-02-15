Documentation for MedianFilter and RangeFilter
==============================================

Overview
---------
RangeFilter:
  A filter object that has an update method which takes in an
  array of length N and returns an array with values in the min-max range

MedianFilter:
  A filter object that has an update method which takes in an
  array of length N and a number D of last number of scans and returns
  an array of the median of the current and previous D arrays

===============================================

Methods
--------
RangeFilter:
  update(arr):
    takes in an array(arr) and returns filter(arr)
  filter(arr):
    modifies an array to contain values in the interval from min to max

MedianFilter:
  update(arr, D):
    takes in an array (arr) and a number of previous scans(arrays to look at)
    as D, and then calls filter(arr) with the array that was passed in
    combined with the previous D number of arrays in arrayCollection,

    Side Result: updates arrayCollection to include passed in array

  filter(arr):
    takes in a 2D array, and returns back an array which contains
    the median of the respective indexes between each array

Installation
------------

Download MedianFilter.py and RangeFilter.py
  to use MedianFilter:
    at the top of a python file include "from MedianFilter import MedianFilter"
  to use RangeFilter:
    at the top of a python file include "from RangeFilter import RangeFilter"

  then to create a filter object, have
    object = MedianFilter()
      or
    object = RangeFilter()
