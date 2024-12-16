QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot  
and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.  


### How does QuickSort Algorithm work?  
QuickSort works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.  

#### There are mainly three steps in the algorithm:  

**1 Choose a Pivot:** Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).  
**2 Partition the Array:** Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.  
**3 Recursively Call:** Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).  
**4 Base Case:** The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.  

#### Here’s a basic overview of how the QuickSort algorithm works.
![image](https://github.com/user-attachments/assets/dc868d60-5e00-4e75-bbf0-2d7f3eac6352)

![Sorting_quicksort_anim](https://github.com/user-attachments/assets/41671eb2-8078-46c2-a44b-480fbe28f057)
