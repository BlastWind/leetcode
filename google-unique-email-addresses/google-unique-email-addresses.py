from operator import indexOf
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # parse each email into clean state
        # add to hashset
        def clean(email: str) -> str:
            localName = email[:email.find('@')]
            domainName = email[email.find('@'):]
            plusIndex = email.find('+')
            return (localName if plusIndex == -1 else localName[:plusIndex]).replace('.', '') + '@' + domainName
        s = set()
        for email in emails:
            s.add(clean(email))
        return len(s)
        # return len hashset


driver = Solution()
print(driver.numUniqueEmails(
    ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
