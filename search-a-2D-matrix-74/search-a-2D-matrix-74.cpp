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
	bool searchMatrix(vector<vector<int>> &matrix, int target)
	{
		int row = 0;
		// first, locate row
		int lo = 0, hi = matrix.size() - 1;
		while (lo < hi)
		{
			int mid = (lo + hi) / 2;
			if (matrix[mid][0] < target)
				lo = mid + 1;
			else
				hi = mid;
		}

		if (lo == 0 && target < matrix[lo][0])
			return false;

		if (target >= matrix[lo][0])
			row = lo;
		else
			row = lo - 1;

		lo = 0, hi = matrix[row].size() - 1;
		while (lo <= hi)
		{
			int mid = lo + (hi - lo) / 2;
			if (matrix[row][mid] == target)
				return true;
			if (matrix[row][mid] < target)
				lo = mid + 1;
			else
				hi = mid - 1;
		}

		return false;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	return 0;
}
