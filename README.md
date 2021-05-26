#  Sorting-Visualizer

##  Different Sorting Algorithms visualization using pygame!

###  Algorithm Implemented:

- Bubble Sort

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
	Time Complexity : 
	```
    	O(n^2)
	```
	Space Complexity:
	```
		O(2)
	```