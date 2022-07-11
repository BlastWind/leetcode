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
	bool isValid(string s)
	{
		const unordered_map<char, char> map =
			{
				{'[', ']'},
				{'(', ')'},
				{'{', '}'},
			};
		const unordered_map<char, char> reversemap =
			{
				{']', '['},
				{')', '('},
				{'}', '{'},
			};
		stack<char> stack;
		for (char c : s)
		{
			if (map.find(c) != map.end()) // push start delimiters
				stack.push(c);
			else if (reversemap.find(c) != map.end())
			{
				if (stack.size() == 0 || stack.top() != reversemap.at(c)) // if the last pushed is not the opening parenthesis of the current, false!
					return false;
				stack.pop();
			}
		}

		return stack.size() == 0;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	cout << a.isValid("]") << endl;
	return 0;
}
