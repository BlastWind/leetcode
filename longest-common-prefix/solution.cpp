#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

class Solution
{
public:
	string longestCommonPrefix(vector<string> &strs)
	{
		if (strs.size() == 0)
			return "";
		// compare the ith letter of all strings, use the ith letter of the 1st string to check
		// if the string doesn't even have an ith letter, exit early, we have the max prefix
		// if the ith letter isn't equal, return the [0 ... i-1] string

		int shortestLength = INT32_MAX;
		for (int i = 1; i < strs.size(); i++)
		{
			shortestLength = std::min(shortestLength, static_cast<int>(strs[i].size()));
		}

		int i = 0;
		// for ith letter
		for (; i < shortestLength; i++)
		{
			// check that all strings have the same letter
			char letter = strs[0][i];
			bool shouldExit = false;
			for (int j = 0; j < strs.size(); j++)
			{
				if (strs[j][i] != letter)
				{
					shouldExit = true;
					break;
				}
			}

			if (shouldExit)
				break;
		}

		return strs[0].substr(0, i);
	}
};

int main()
{
	Solution a;
	vector<string> vectorOfStrings = {""};
	printf("%s", a.longestCommonPrefix(vectorOfStrings).c_str());
}