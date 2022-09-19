from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        # [4, 2, 2, 7, 2, 4, 13], maxWidth 16
        # if len(word) == maxWidth or len(word) + 1 + len(nextWord) > maxWidth: DONE
        # while len(word) + 1 + nextWord <= maxWidth, add add next word to current
        # Justify at the end of each iteration:
        # spacesLeft = maxWidth - sum(map(len, lineWords))
        # spacesLeft // len(lineWords) // spaces I can give to each word
        # spacesLeft % len(lineWords) // spaces I can give to each word left to right
        i = 0
        while i < len(words):
            if i == len(words) - 1:
                res.append(words[i] + ' ' * (maxWidth - len(words[i])))
                i += 1
                continue
            firstWord = words[i]

            if len(firstWord) == maxWidth or len(firstWord) + 1 + len(words[i+1]) > maxWidth:
                # line only has space for 1 word
                res.append(words[i] + ' ' * (maxWidth - len(words[i])))
                i += 1
                continue
            counter = maxWidth
            j = i
            # > and not >=, because require one ' ' after each word
            while j < len(words) and counter - len(words[j]) >= 0:
                counter -= (len(words[j]) + 1)
                j += 1

            lineWords = words[i:j]

            spacesLeft = maxWidth - sum(map(len, lineWords))
            if j == len(words):
                build = ""
                for word in lineWords[:-1]:
                    build += word + ' '
                build += lineWords[-1]
                build += ' ' * (spacesLeft - len(lineWords)+1)
                res.append(build)
                return res
            # - 1 because Don't need to give right space for last word
            spaceEach = spacesLeft // (len(lineWords) - 1)
            extraSpaces = spacesLeft % (len(lineWords) - 1)
            build = ''
            for k, word in enumerate(lineWords):
                if k == len(lineWords) - 1:
                    build += word
                elif extraSpaces > 0:
                    build += (word + ' ' * (spaceEach + 1))
                    extraSpaces -= 1
                else:
                    build += (word + (' ' * (spaceEach)))
            res.append(build)
            i += len(lineWords)
        return res


driver = Solution()
print(driver.fullJustify(
    ["ask", "not", "what", "your", "country", "can", "do", "for", "you",
        "ask", "what", "you", "can", "do", "for", "your", "country"],
    17))
