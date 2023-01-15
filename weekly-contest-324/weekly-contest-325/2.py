class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # find the indices of the first k a's, b's, and c's from the left
        # find the indices of the first k a's, b's, and c's from the right


        # what about "aabaaaacaabc",  k = 2?


        # First, first ranges from each side that would meet satisfy
        # From left, the range is therefore the entire string
        # From right, the range is "__baaaacaabc"

        # Now, remove element at a time 
        

        # if there was equal situation, we might backtrack later
        # else, if one is definitely needed, pick that one?

        # aabbbbbccbbbbbbbbbbbbbbbbbbbbcab

        return 0