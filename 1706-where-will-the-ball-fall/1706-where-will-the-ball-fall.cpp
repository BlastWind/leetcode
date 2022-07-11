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
	vector<int> findBall(vector<vector<int>> &grid)
	{
		vector<int> results;
		int m = grid.size();
		int n = grid[0].size();
		// from each column, a ball is dropped (like connect 4)
		for (int ball = 0; ball < n; ball++)
		{
			int col = ball;
			bool stuck = 0;
			for (int row = 0; row < m; row++)
			{
				if (grid[row][col] == -1)
				{
					if (col == 0 || grid[row][col - 1] == 1)
					{
						stuck = 1;
						break;
					}
					col -= 1;
				}
				if (grid[row][col] == 1)
				{
					if (col == n - 1 || grid[row][col + 1] == -1)
					{
						stuck = 1;
						break;
					}
					col += 1;
				}
			}
			results.emplace_back(stuck ? -1 : col);
		}
		return results;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<vector<int>> grid{{-1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1}};

	for (auto i : a.findBall(grid))
	{
		cout << i << ", ";
	}
	cout << endl;
	return 0;
}
