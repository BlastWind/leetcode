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
	template <typename T>
	T findDuplicateBinarySearch(vector<T> &arr) // handsome cpp, but O(n log n)
	{
		// note that in a sorted arr, arr.map(small_or_equal) is monotonic
		auto small_or_equal = [&](T cur)
		{
			int count = 0;
			for (auto &ele : arr)
			{
				if (ele <= cur)
					count++;
			}
			return count;
		};

		int low = 1, high = arr.size(); // not [0, n-1] because ranging [1, n]
		T duplicate;
		while (low <= high)
		{
			int cur = (low + high) / 2; // note that binary search usually accesses arr[mid]. But here, I don't. The [1, ..., n] is the array
			if (small_or_equal(cur) > cur)
			{
				high = cur - 1;
				duplicate = cur;
			}
			else
				low = cur + 1;
		}
		return duplicate;
	}
	template <typename T>
	T findDuplicateTortoiseAndHare(vector<T> &arr)
	{
		}
};

int main(int argc, char *argv[])
{
	Solution a;
	return 0;
}
