#include <vector>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
using namespace std;
class Solution
{
public:
	int findDuplicate(vector<int> &nums)
	{
		for (int i = 0; i < nums.size(); i++)
		{
			int flipAt = abs(nums[i]);
			if (nums[flipAt] <= 0)
				return flipAt;
			nums[flipAt] *= -1;
		}

		return -1;
	}
};

int main()
{
	vector<int> a = {1, 3, 4, 2, 2};
	Solution b;
	printf("%d", b.findDuplicate(a));
}