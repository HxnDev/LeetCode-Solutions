# Text Justification Problem

Given an array of words and a width **maxWidth**, format the text such that each line has exactly *maxWidth* characters and is fully [left and right] justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ``` ' ' ``` when necessary so each line has exactly *maxWidth* characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, then empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no **extra** space is inserted between words.

### Note:

- A word is defined as characyer sequence consisitng of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed *maxWidth*
- The input array *words* contains atleast one word.

### Example 1:
```
INPUT: words = ["This", "is", "an", "example", "of", "text", "justification"], maxWidth = 16
OUTPUT: 
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```

### Example 2:
```
INPUT: words = ["What", "must", "be", "acknowledgement", "shall", "be"], maxWidth = 16
OUTPUT: 
[
  "What   must    be",
  "acknowledgement  ",
  "shall be.        "
]
```

### Example 3:
```
INPUT: words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth = 20
OUTPUT: 
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

