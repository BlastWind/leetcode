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
	int ROW, COL;

public:
	int numEnclaves(vector<vector<int>> &grid)
	{
		int num = 0;
		ROW = grid.size();
		COL = grid[0].size();
		vector<int> rowBorders = {0,
								  ROW - 1};
		vector<int> colBorders = {0, COL - 1};

		for (int i = 0; i < rowBorders.size(); i++)
		{
			for (int j = 0; j < grid[0].size(); j++)
			{
				dfs(grid, rowBorders[i], j);
			}
		}

		for (int i = 0; i < grid.size(); i++)
		{
			for (int j = 0; j < colBorders.size(); j++)
			{
				dfs(grid, i, colBorders[j]);
			}
		}

		for (int i = 0; i < grid.size(); i++)
		{
			for (int j = 0; j < grid[0].size(); j++)
			{
				if (grid[i][j] == 1)
				{
					num++;
				}
			}
		}

		return num;
	}
	void dfs(vector<vector<int>> &a, int i, int j);
	// cleans borders
	void dfs(vector<vector<int>> &grid, int row, int col)
	{
		if (row < 0 or col < 0 or row > grid.size() - 1 or col > grid[0].size() - 1)
		{
			return;
		}

		if (grid[row][col] == 0)
		{
			return;
		}

		grid[row][col] = 0;

		dfs(grid, row, col + 1);
		dfs(grid, row, col - 1);
		dfs(grid, row + 1, col);
		dfs(grid, row - 1, col);
	}
};
int main(int argc, char *argv[])
{
	Solution a;
	vector<vector<int>> grid{{0, 0, 0, 0}, {1, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}};
	a.numEnclaves(grid);

	int b = grid.size();
	return 0;
}
