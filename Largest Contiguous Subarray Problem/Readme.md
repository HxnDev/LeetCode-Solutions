# Largest Contiguous Subarray Problem

Given an array of integers *nums* and an integer *target*, return the **indices of the two numbers such that they add upto the *target***.

You may assume that each input would have ***exactly one solution***, and you may not use the same element twice.

You can return the answer in any order/

### Example 1:
```
INPUT: nums = [7,7,11,15], target = 9
OUTPUT: [0,1]
EXPLANATION: Because nums[0] + nums[1] == 9, so we return [0,1].
```

### Example 2:
```
INPUT: nums = [3,2,4], target = 6
OUTPUT: [1,2]
```

### Example 3:
```
INPUT: nums = [3,3], target = 6
OUTPUT: [0,1]
```

### Constraints:

- ``` 2 <= nums.length <= 10^4 ```
- ``` -10^9 <= nums[i] <= 10^9 ```
- ``` -10^p <= target <= 10^9 ```
- **Only one valid answer exists**
