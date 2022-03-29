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
	/*
	Algo:
		Just keep dfs-ing down the cell. If it ever gets to the edge, return 0 because not island, else return 1
	 */
	int closedIsland(vector<vector<int>> &grid)
	{
		int islands = 0;
		for (int i = 0; i < grid.size(); i++)
		{
			for (int j = 0; j < grid[0].size(); j++)
			{
				if (grid[i][j] == 0)
					islands += dfs(grid, i, j);
			}
		}
		return islands;
	}

	int dfs(vector<vector<int>> &grid, int row, int col)
	{
		if (row < 0 or col < 0 or row > grid.size() - 1 or col > grid[0].size() - 1)
		{
			return 0;
		}
		if (grid[row][col] > 0)
		{
			return 1;
		}
		grid[row][col] = 2;

		return dfs(grid, row, col + 1) * dfs(grid, row, col - 1) * dfs(grid, row + 1, col) * dfs(grid, row - 1, col);
	}
};
int main(int argc, char *argv[])
{
	Solution a;
	vector<vector<int>> v{
		{1, 1, 1, 1, 1, 1, 1, 0}, {1, 0, 0, 0, 0, 1, 1, 0}, {1, 0, 1, 0, 1, 1, 1, 0}, {1, 0, 0, 0, 0, 1, 0, 1}, {1, 1, 1, 1, 1, 1, 1, 0}};
	return a.closedIsland(v);
}
