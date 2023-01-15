from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter_1, counter_2 = Counter(word1), Counter(word2)
        diff = abs(len(counter_1) - len(counter_2))

        # if diff == 0
        # Does not work if
        # word1 has no duplicates but word2 only has duplicates, yet there are no overlapped characters between the two words, vice versa
        print(counter_1.values(), counter_2.values())
        if diff == 0:
            return not ((all(v == 1 for v in counter_1.values()) and all(v > 1 for v in counter_2.values()) and len(set(counter_1.keys()).intersection(set(counter_2.keys()))) == 0)
                        or (all(v == 1 for v in counter_2.values()) and all(v > 1 for v in counter_1.values()) and len(set(counter_2.keys()).intersection(set(counter_1.keys()))) == 0))

        # if diff is >2
        # more distinct must give

        # aabc |  -> aebc | adaf
        if diff > 2:
            return False

        more_distinct = max([counter_1, counter_2], key=len)
        less_distinct = min([counter_1, counter_2], key=len)

        # diff is 2
        # Condition: the more distinct string can give a duplicate that is unique to the less distinct string
        # AND the less distinct string has something to give that is not unique to the more distinct

        # OR
        # The more distinct can give off a unique one and receive a duplicate
        if diff == 2:
            for k, v in more_distinct.items():
                if v == 1 and k not in less_distinct:
                    return True

        # diff is 1
        if diff == 1:
            # Condition #1: the more distinct string has a duplicate to spare that is not found in the less distinct string
            # Condition #2: the less distinct string has a duplicate character that is already found in the more distinct string
            for k, v in more_distinct.items():
                if v > 1 and k not in less_distinct:
                    break
            else:  # didn't find one
                return False

            for k, v in less_distinct.items():
                if v > 1 and k in less_distinct:
                    break
            else:
                return False

            return True

        print("shouldn't be here")
        return False

        # aabbcc
        # abcde

        # swap -> aabbcd | abcce

    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1, freq2 = Counter(word1), Counter(word2)
        len1, len2 = len(freq1), len(freq2)
        import string

        for c1 in string.ascii_lowercase:
            for c2 in string.ascii_lowercase:
                if c1 not in freq1 or c2 not in freq2:
                    continue

                # edge: c1 == c2. Edge, because later algorithm doesn't consider
                # that the letter going out could be the letter coming in, and therefore
                # requires another round of checking, but we avoid that.
                if c1 == c2:
                    if len1 == len2: return True
                else:
                    cnt1, cnt2 = len1, len2
                    if freq1[c1] == 1:
                        cnt1 -= 1
                    if freq1[c2] == 0:
                        cnt1 += 1
                    if freq2[c2] == 1:
                        cnt2 -= 1
                    if freq2[c1] == 0:
                        cnt2 += 1
                    if cnt1 == cnt2:
                        print(c1, c2)
                        return True

        return False


print(Solution().isItPossible("aa", "ab"))
