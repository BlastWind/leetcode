#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

using namespace std;
class Solution
{
public:
	int lengthOfLongestSubstring(string s)
	{
		if (s.length() == 0)
			return 0;

		// slide window: Slide window right if rightmost entry is nonrepeating
		// If rightmost entry is repeating, shrink leftmost entry until rightmost entry is no longer repeating
		unordered_map<char, int> umap;

		int left = 0, right = 0, len = 0, maxlen = 0;
		while (right <= s.length() - 1)
		{
			if (umap.find(s[right]) == umap.end()) // rightmost entry is nonrepetaing
			{
				umap.insert(make_pair(s[right], 1));
				len++;
				right++;
				maxlen = max(maxlen, len);
			}
			else if (umap[s[right]] == 0)
			{
				umap[s[right]]++;
				len++;
				right++;
				maxlen = max(maxlen, len);
			}
			else
			{
				while (umap[s[right]] != 0) // remove until right is nonoffending
				{
					umap[s[left]]--;
					left++;
					len--;
				}
			}
		}
		return maxlen;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	cout << a.lengthOfLongestSubstring("b") << endl;
	return 0;
}
