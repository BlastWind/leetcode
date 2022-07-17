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
		if (n == 0)
			return tasks.size();
		int leastInterval = 0;
		unordered_map<char, int> freqTable;
		for (auto task : tasks)
			freqTable[task]++;

		// algorithm: We want to keep performing alternate tasks until task frequencies are 0
		// So push initial frequencies
		// 1) We must wait n steps before executing potentially the same item again
		// 2) During this waiting interval, we try to execute some many alternate tasks as possible

		// To encode both 1) and 2), have a while loop that adds (n+1) steps at the end of each iteration
		// (to simulate the wait n steps), and, this loop tries to cycle the queue.
		// If the frequencies queue has less elements than n, then, we cycle as many as we can and wait the remainding time
		// If the frequencies queue have more elements than n, then, we can cycle through n elements, that's nice.

		// Note that a priority queue is used so the task with the largest frequencies is always executed first.
		// This is needed, for example, let's consider the situation if we have tasks c, d, a, a, b, b and n = 5
		// Then, frequencies are [1, 1, 2, 2]. Now, if priority queue not used, we issue the wait at the 1's, so it kinda becomes
		// [0, 0, 1, 1, wait, wait, go again]. But, we shouldn't be able to go able. There isn't enough space
		// between the second round's 1 and the go again. On the other hand, if we use a priority queue, this prob is avoided.

		priority_queue<int> q;
		for (auto pair : freqTable)
			q.push(pair.second);
		while (!q.empty())
		{
			vector<int> tempFreq;
			for (int i = 0; i <= n; i++) // cycle through at most n
			{
				if (q.empty())
					break;
				tempFreq.push_back(q.top());
				q.pop();
			}
			for (int i : tempFreq)
				if (--i > 0)
					q.push(i);
			leastInterval += q.empty() ? tempFreq.size() : n + 1; // if already done, no need to wait for n + 1
		}
		return leastInterval;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<char> v{'a', 'b', 'c', 'c'};
	a.leastInterval(v, 8);
	return 0;
}
