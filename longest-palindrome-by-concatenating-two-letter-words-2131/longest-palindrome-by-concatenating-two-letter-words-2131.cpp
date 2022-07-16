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
	int longestPalindrome(vector<string> &words)
	{

		int len = 0;
		int freqTable[26][26] = {{0}};
		// preprocessing words into freqTable. Note that we can be "greedy" and already start checking for flipped words
		for (auto word : words)
		{
			// if flipped word exists already in table:
			if (freqTable[word[1] - 'a'][word[0] - 'a'] > 0)
			{
				len += 4;
				freqTable[word[0] - 'a'][word[1] - 'a']--;
			}
			else
				freqTable[word[0] - 'a'][word[1] - 'a']++;
		}

		for (int i = 0; i < 26; i++)
			if (freqTable[i][i] > 0)
				return len + 2;
		return len;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<string> words({"dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"});
	cout << a.longestPalindrome(words);
	return 0;
}
