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
	vector<vector<string>> partition(string s)
	{
		// 1) Think when are decisions exhausted
		// when there is no more string to split to make a palindrome
		// 2) Think what decisions are possible at each config
		// given a letter, try including it

		// if the current word is a palindrome
		// either push it or keep adding to it to find a longer palindrome

		// if we push it,

		// every time there is a palindrome, create new vector
		// and recur with a reference to it

		// every time

		/* config includes last palindrome end location,
			current index
			vector to push into
			parent 2d vector

		*/

		// 2dvec.push(recur(...))
		vector<vector<string>> twodvec;
		vector<string> emptyVec;
		recur(twodvec, emptyVec, s, 0, 0);
		return twodvec;
	}

	void recur(vector<vector<string>> &twodvec, vector<string> &partitions, string &s, int lastEndLoc, int curLoc)
	{
		printf("%s lastEndLoc %i curLoc %i\n", s.substr(lastEndLoc, curLoc - lastEndLoc).c_str(), lastEndLoc, curLoc);
		if (curLoc == s.length())
		{
			if (!isPalindrome(s.substr(lastEndLoc, curLoc - lastEndLoc)))
				return;

			partitions.push_back(s.substr(lastEndLoc, curLoc - lastEndLoc));
			if (partitions.size() > 0)
			{
				twodvec.push_back(partitions);
			}
			partitions.pop_back();
			return;
		}
		if (isPalindrome(s.substr(lastEndLoc, curLoc - lastEndLoc)))
		{
			partitions.push_back(s.substr(lastEndLoc, curLoc - lastEndLoc));
			recur(twodvec, partitions, s, curLoc, curLoc + 1);
			partitions.pop_back();
		}

		recur(twodvec, partitions, s, lastEndLoc, curLoc + 1);
		return;
	}

	bool isPalindrome(string S)
	{
		// Stores the reverse of the
		// string S
		string P = S;

		// Reverse the string P
		reverse(P.begin(), P.end());

		// If S is equal to P
		if (S == P)
		{
			// Return "Yes"
			return true;
		}
		// Otherwise
		else
		{
			// return "No"
			return false;
		}
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	a.partition("cdd");
	printf("%i", a.isPalindrome("aab"));
	return 0;
}
