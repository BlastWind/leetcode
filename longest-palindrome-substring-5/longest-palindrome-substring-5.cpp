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
	string longestPalindrome(string s)
	{
		int dp[s.length()][s.length()], left = 0, maxlen = 0;
		memset(dp, 0, s.length() * s.length() * sizeof(int));
		for (int i = 0; i < s.length(); i++)
			dp[i][i] = 1;
		for (int i = 0; i < s.length() - 1; i++)
		{
			if (s[i] == s[i + 1])
			{
				dp[i][i + 1] = 1;
				left = i;
				maxlen = 1;
			}
			else
				dp[i][i + 1] = 0;
		}

		for (int i = 2; i < s.length(); i++)
		{
			for (int j = i; j < s.length(); j++)
			{
				// j-i, j
				dp[j - i][j] = (dp[j - i + 1][j - 1] && s[j - i] == s[j]);
				if (dp[j - i][j] == 1 && maxlen < i)
				{
					// printf("j: %d, j+i: %d, new left: %d, new maxlen: %d", j, j + 1, left, maxlen);
					left = j - i;
					maxlen = i;
				}
			}
		}

		return s.substr(left, maxlen + 1);
	}
	string expansionLongestPalindrome(string s)
	{
		if (s.length() < 1)
			return "";
		int start = 0, end = 0;
		for (int i = 0; i < s.length(); i++)
		{
			int len1 = expandAroundCenter(s, i, i);
			int len2 = expandAroundCenter(s, i, i + 1);
			int len = max(len1, len2);
			if (len > end - start)
			{
				start = i - (len - 1) / 2;
				end = i + len / 2;
			}
		}
		return s.substr(start, end + 1 - start);
	}

	int expandAroundCenter(string s, int left, int right)
	{
		int L = left, R = right;
		while (L >= 0 && R < s.length() && s[L] == s[R])
		{
			L--;
			R++;
		}
		return R - L - 1;
	}
	string fastlongestPalindrome(string s)
	{
		const int n = s.size();
		if (n == 0)
			return "";
		int dp[n][n], maxlen = 1, left = 0; // maxlen = 1 when only one word
		memset(dp, 0, n * n * sizeof(int));
		for (int i = 0; i < n; ++i)
		{
			dp[i][i] = 1;
			for (int j = 0; j < i; ++j)
			{
				printf("%d,%d\n", j, i);
				dp[j][i] = (s[j] == s[i] && (i - j < 2 || dp[j + 1][i - 1]));
				if (dp[j][i] && maxlen < i - j + 1)
				{
					left = j;
					maxlen = i - j + 1;
				}
			}
		}
		return s.substr(left, maxlen);
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	string pld = a.expansionLongestPalindrome(
		"cbbd");
	cout << "Max: " << pld << endl;
	return 0;
}
