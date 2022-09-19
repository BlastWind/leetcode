Initially, I calculated the prefix sums. Then, I run two nested for loops through the prefix sum array
in order to calculate the sum of each subsequence. This is O(n^2), which gives TLE for my python solution.

So, I attempted to optimize with a hashmap (value: freq count). I store results into hashmap and try to find the difference between
the current element and the provided element just like in two-sum. However, the implementation was quite hard: 
I need to keep track of the indices, diff different indices array, blah blah blah...

So I looked up the solution: 

Ah, hashmap optimization is clean, but, it will be cleaner to build up the hashmap and calculate results 
INCREMENTALLY. This works because at each step, looking into the hashmap only looks at the frequency counts
of the elements traversed thus far. This perfectly avoids having to keep an indices array just to figure out
the array diffs and results at the end (very messy).



