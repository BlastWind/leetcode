#include <vector>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution
{
public:
	int maxSubArray(vector<int> &nums)
	{
		int DP[nums.size()];
		DP[0] = nums[0];
		for (int i = 1; i < nums.size(); i++)
		{
			DP[i] = max(DP[i - 1] + nums[i], nums[i]);
		}
		int max = INT_MIN;
		for (int i = 0; i < nums.size(); i++)
		{
			max = std::max(max, DP[i]);
		}
		return max;
	}
};

int main()
{
	Solution a;
	vector<int> nums = {3, 4, 5, -1, 2};
	printf("%d", a.maxSubArray(nums));
}