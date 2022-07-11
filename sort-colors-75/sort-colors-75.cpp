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
	void sortColors(vector<int> &nums)
	{
		// sort into [ 0..0 1..1 2..2]
		int zeroPtr = 0, twoPtr = nums.size() - 1;
		for (int i = 0; i < nums.size() && i <= twoPtr; i++)
		{
			int cur = nums[i];
			if (cur == 0)
			{
				swap(nums, zeroPtr, i);
				// if (nums[zeroPtr] != 0)
				zeroPtr++;
			}
			else if (cur == 2)
			{
				swap(nums, twoPtr, i);
				// if (nums[twoPtr] != 2)
				twoPtr--;
				i--;
			}
		}
	}
	template <typename T>
	void swap(vector<T> &arr, int one, int two)
	{
		auto temp = arr[one];
		arr[one] = arr[two];
		arr[two] = temp;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<int> b{
		1, 2, 0,
		1,
		1,
		0,
		2, 0, 0, 2, 1, 2};
	a.sortColors(b);
	for (auto c : b)
	{
		cout << c << endl;
	}
	return 0;
}
