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
	int numEnclaves(vector<vector<int>> &grid)
	{
		int num = 0;
		for (int i = 0; i < grid.size(); i++)
		{
			for (int j = 0; j < grid[0].size(); j++)
			{
				int hey = 0;
				if ((hey = dfs(grid, i, j)) == -1)
				{
					continue;
				}
				num += hey;
			}
		}

		return num;
	}

	int dfs(vector<vector<int>> &grid, int row, int col)
	{
		if (row < 0 or col < 0 or row > grid.size() - 1 or col > grid[0].size() - 1)
		{
			return -1;
		}

		if (grid[row][col] == 0)
		{
			return 0;
		}

		grid[row][col] = 0;

		int a = dfs(grid, row, col + 1);
		int b = dfs(grid, row, col - 1);
		int c = dfs(grid, row + 1, col);
		int d = dfs(grid, row - 1, col);
		if (a == -1 || b == -1 || c == -1 || d == -1)
		{
			return -1;
		}
		return 1 + a + b + c + d;
	}
};
int main(int argc, char *argv[])
{
	Solution a;
	vector<vector<int>> grid{{0, 0, 0, 0}, {1, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}};
	a.numEnclaves(grid);
	return 0;
}
