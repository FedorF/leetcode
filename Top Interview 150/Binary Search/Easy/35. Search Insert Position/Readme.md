## 35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
```
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 10e4 <br>
-10e4 <= nums[i] <= 10e4 <br>

nums contains distinct values sorted in ascending order. <br>
-10e4 <= target <= 10e4
```

## Solution.
1) Only distinct values 
![1](img1.png)

2) With duplicates.
![2](img2.png)

