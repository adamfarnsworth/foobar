## Level 1
### Prison Labor Dodgers

Commander Lambda is all about efficiency, including her
bunny prisoners for manual labor.  But no one's been properly
monitoring the labor shifts for a while, and the've gotten
quite mixed up.  You've been given the task of fixing them, but
after you wrote up new shifts, you realized that some prisoners
had been transferred to a different block and aren't available
for their assigned shifts.  Aand maually sorting though each
shift list to compare against prisoner block lists will take
forever - remember, Commander Lambda loves efficiency!  

 Given two almost identical lists of prisoner IDs x and y where
 one of the lists contains an additional ID, write a function
 answer(x,y) that compares the lists and returns the additional
 ID.  
 
 For example, given the list x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13],
 the function answer(x,y) would return 6 because the
 list x contains the integer 6 and the list y dosen't.  Given the
 list x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50],
 the function answer(x,y) would return -4
 because the list y contains the integer -4 and the list x
 doesn't.  
 
 In each test case, the list x and y will always contain n non-
 unique integers where n is at least 1 but never more than 99,
 and one of the lists will contain an additional unique integer
 which should be returned bt the function.  The same n non-
 unique integers will be present on both lists, but they might
 appear in a different order, like in the examples above.
 Commander Lambda likes to keep ehr numbers short, so every
 prisioner ID will be between -1000 and 1000.  
 
 ## Test cases
 ### Inputs:
 ```python
x = [13,5,6,2,5]  
y = [5,2,5,13]  
```
### Output:
 ```python
6  
```
 ### Inputs:
  ```python
x = [14,27,1,4,2,50,3,1]  
y = [2,4,-4,3,1,1,14,27,50]  
```
### Output:
 ```python
-4  
```
