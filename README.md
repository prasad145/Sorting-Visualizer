#  <ul>Sorting-Visualizer</ul>
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br/>
Different Sorting Algorithms visualization using pygame!


#  Algorithms Implemented:

## [Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
```
procedure bubbleSort( list : array of items )
loop = list.count;
for i = 0 to loop-1 do:
swapped = false
for j = 0 to loop-1 do:
/* compare the adjacent elements */
if list[j] > list[j+1] then
/* swap them */
swap( list[j], list[j+1] )
swapped = true
end if
end for
/*if no number was swapped that means array is sorted now, break the loop.*/
if(not swapped) then
break
end if
end for
end procedure return list
```
#### Time Complexity : 
```
O(n^2)
```
#### Space Complexity:
```
O(2)
```

## [Quick Sort (Random Pivot)](https://www.geeksforgeeks.org/quick-sort/)
	
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

	*  Always pick first element as pivot
	*  Always pick last element as pivot
	* Pick a random element as pivot (efficeint)

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.
```
partition(arr[], lo, hi) 
pivot = arr[hi]
i = lo - 1     // place for swapping
for j := lo to hi – 1 do
if arr[j] < pivot then
i = i + 1
swap arr[i] with arr[j]
swap arr[i] with arr[hi]
return i

partition_r(arr[], lo, hi)
r = Random Number from lo to hi
Swap arr[r] and arr[hi]
return partition(arr, lo, hi)

quicksort(arr[], lo, hi)
if lo < hi
p = partition_r(arr, lo, hi)
quicksort(arr, lo , p-1)
quicksort(arr, p+1, hi)
```
#### Time Complexity : 
```
O(n logn)
```
#### Space Complexity:
```
O(n)
```
## [Merge Sort](https://www.geeksforgeeks.org/merge-sort/)
Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
```
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
```
#### Time Complexity : 
```
O(n logn)
```
#### Space Complexity:
```
O(n)
```
