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
	vector<int> findSubstring(string s, vector<string> &words)
	{
		unordered_map<string, int> table;
		// build frequency table
		for (string word : words)
		{
			table[word]++;
		}
		unordered_map<string, int> reference(table);
		vector<int> ans;
		int wordsCount = words.size();
		int wordSize = words[0].length();
		vector<int> result;
		if (wordsCount == 0)
			return ans;

		int maxWindowSize = wordsCount * wordSize;
		if (s.length() < maxWindowSize)
			return ans;

		// we can start windows from # words beginnings
		// in each window, we extend left and right only by word length each time
		for (int i = 0; i < wordSize; i++)
		{
			// window starting from i
			table = reference;
			int left = i;
			int right = left;
			while (right - left < maxWindowSize && right + wordSize <= s.size())
			{
				string newWord = s.substr(right, wordSize);
				// TABLE=REFERENCE SLOWNESS
				if (table.count(newWord) == 0) // If DNE (does not exist), skip till after
				{
					// skip over, restore table
					for (int i = left; i <= right; i += wordSize)
					{
						string iterWord = s.substr(i, wordSize);
						if (table.count(iterWord) == 1)
							table[iterWord]++;
					}
					left = right + wordSize;
					right = left;
					// table = reference; // If there is a lot of DNE, yet, the steps skipped isn't large enough, this is bad
					continue;
				}
				if (table[newWord] == 0) // If excessive word, skip till we get rid of the earliest newWord matched from the front
				{
					int iter = left;
					string iterWord = "";
					while ((iterWord = s.substr(iter, wordSize)) != newWord)
					{
						table[iterWord]++;
						iter += wordSize;
					}
					// left now pointers after the first excess word from the front
					left = iter + wordSize;
					table[iterWord]++;
					continue;
				}
				table[newWord]--;
				right += wordSize;
				if (right - left == maxWindowSize) // if control flow reaches here, definitely a match
				{

					ans.push_back(left);
					string firstWord = s.substr(left, wordSize);
					left += wordSize;
					table[firstWord]++;
				}
			}
		}
		return ans;
	}
};

int main(int argc, char *argv[])
{
	Solution a;

	// string s = "a";
	// vector<string> words = {"a", "a"};

	// string s = "wordgoodgoodgoodbestwordword";
	// vector<string> words = {"word", "good", "best", "word"};

	string s = "acccaccaa";
	vector<string> words{"aa", "cc", "ca"};
	for (auto index : a.findSubstring(s, words))
		cout
			<< index << ", ";
	return 0;
}
