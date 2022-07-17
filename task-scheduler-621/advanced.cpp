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
	int leastInterval(vector<char> &tasks, int n)
	{
		// if no idle units, return tasks (minimum)

		// lower bound is (maxcnt-1) * (n+1) + e, where e = #tasks with frequencies maxcnt
		// Intuition: we need to queue at least maxcnt rounds, where each round can executes/waits for (n+1) elements
		// The maxcnt - 1 comes from the fact that the last round does not need waiting
		// If there is only one element with maxcnt, then the last ronud execute e = 1, if two, then e = 2...

		int freq[26] = {0}, maxcnt = 0, e = 0;
		for (auto task : tasks)
			freq[task - 'A']++; // - 'A' because task can only be upper case
		for (int i = 0; i < 26; i++)
			maxcnt = max(maxcnt, freq[i]);
		for (int i = 0; i < 26; i++)
			if (freq[i] == maxcnt)
				e++;
		return max((int)tasks.size(), (maxcnt - 1) * (n + 1) + e);
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<char> v{'A', 'A', 'A', 'B', 'B', 'B'};

	cout << a.leastInterval(v, 2);
	return 0;
}
