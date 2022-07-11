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
	int maxArea(vector<int> &height)
	{
		int start = 0, end = height.size() - 1;
		int maxArea = 0;
		while (start < end)
		{
			maxArea = max(maxArea, (end - start) * min(height[start], height[end]));
			if (height[start] < height[end])
				start++;
			else
				end--;
		}
		return maxArea;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<int> b{1, 1};
	cout << a.maxArea(b) << endl;
	return 0;
}
