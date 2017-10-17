Recursive list Sorting

conditions -
1. make all functions using recursion
2. You do not have to return a list
3. Dont use a loop
4. Sorting with ascending order only.


INSERTION SORT 

1. 
File name : insert_in_sorted_list.py
Objective : Insert an element in a sorted List from 0 to len(list) 
approach  : compare the element to the sorted_list[index]
			If greater, move forward with recursion
			If not, insert it at that position
			If the index reaches to the end of list, append the element

2. 
File name : mysort-del-index-tracking-ins.py
Objective : Sorting a list
approach  : finds the anamoly index, deletes the current element from unsorted subarray 
			and inserts at the anamoly index in the sorted subarray


3. 
File name : insert_in_sorted_sublist.py
Objective : Insert an element in a sorted sublist from 0 to i
approach  : compare the element to the sorted_list[index]
    		If greater, move forward with recursion, If not, insert it at that position. 
    		If the index reaches to the end of list, perform a check, 
    		whether the existing end element is greater or smaller than the element to be inserted
    		If the existing element is smaller, insert after it, If greater, insert at that index.


4. File name : mysort-del-insert_in_sorted_sublist.py
   Objective : sorts the list - cw logic
   Logic 	 : use this insert_in_sorted_sublist.py
			   start from starting, if a problem element is found, delete it from that index and 
			   use insert_in_sorted_sublist to insert it in 0 to i in  sorted manner.

5. Filename : insertion_sort_classic.py
   Objective: Implement Standard insertion sort
   approach : Find the anamoly index. Start copying elements from index to index+1, 
   			  until you reach the correct place for anamoly element. Copy anamoly element at the correct place.


SELECTION SORT

6. 
File name : find_index_of_min_of_sublist.py
Objective : find the index of least element between the indices lower to upper
approach  : assume a[lower] to be min element, compare it with all others, if a smaller element is found,
			update the min. Continue this till end of the list. 


7. 
File name : nice-find-min-index.py
Author    : Saurabh bhandari
Objective : find the index of least element between the indices lower to upper
approach  : Assume lower and upper as true list bounds, compare a[lowrer] <= a[upper],
			If true, approach from the upper end by decrementing upper, 
			else,    approach from the lower end by incrementing lower,
			at last, upper and lower meets at the index of min element, return this.


7. 
File name : sort-find_index_of_min_of_sublist-swap.py
Objective : Sort the list
approach  : We start scanning the list from the start, when an abnormality is found,
			we find the index of min element in the un-scanned sublist, then swap the abnormality and min ele,
			we then continue this process till the complete list is scanned.

8. <same as Q7>
File name : selection_sort_classic.py
Objective : Implement the classic selection sort
approach  : We start scanning the list from the start, when an abnormality is found,
			we find the index of min element in the un-scanned sublist, then swap the abnormality and min ele,
			we then continue this process till the complete list is scanned.


