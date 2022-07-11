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
	bool isMatch(string s, string p)
	{
		vector<vector<int>> dp(s.size(), vector<int>(p.size() + 1, -1));
		return match(dp, s, p, 0, 0);
	}
	bool match(vector<vector<int>> &dp, string &s, string &p, int s_index, int p_index)
	{
		if (s_index >= s.size() && p_index >= p.size())
			return true;
		if (p_index >= p.size())
			return false;
		if (dp[s_index][p_index] != -1) // if has been set, return it
			return dp[s_index][p_index];
		bool isMatch = s_index < s.size() && (p[p_index] == '.' || s[s_index] == p[p_index]);
		if (p_index + 1 < p.size() && p[p_index + 1] == '*')
		{
			// try not matching
			return dp[s_index][p_index] = match(dp, s, p, s_index, p_index + 2) || isMatch && match(dp, s, p, s_index + 1, p_index);
		}
		if (isMatch)
			return dp[s_index][p_index] = match(dp, s, p, s_index + 1, p_index + 1);
		return dp[s_index][p_index] = false; // set to 0
	}
};
int main(int argc, char *argv[])
{
	Solution a;
	// cout << a.isMatch("aba", "a*b*a*") << endl;
	// cout << a.isMatch("a", "ab*") << endl;
	// cout << a.isMatch("ab", ".c*") << endl;
	// cout << a.isMatch("a", "ab*a") << endl;

	cout << a.isMatch("mississippi",
					  "mis*is*p*.");
	return 0;
}
