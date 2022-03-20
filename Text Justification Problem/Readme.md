# Text Justification Problem

Given an array of words and a width **maxWidth**, format the text such that each line has exactly *maxWidth* characters and is fully [left and right] justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ``` ' ' ``` when necessary so each line has exactly *maxWidth* characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, then empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no **extra** space is inserted between words.

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
