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
	int maxAreaOfIsland(vector<vector<int>> &grid)
	{
		int area = 0;
		for (int i = 0; i < grid.size(); i++)
		{
			for (int j = 0; j < grid[0].size(); j++)
			{
				if (grid[i][j] != 2)
				{
					area = max(area, dfs(grid, i, j));
				}
			}
		}
		return area;
	}

	int dfs(vector<vector<int>> &grid, int row, int col)
	{
		if (row < 0 or col < 0 or row > grid.size() - 1 or col > grid[0].size() - 1)
		{
			return 0;
		}
		if (grid[row][col] != 1 or grid[row][col] == 2)
		{
			return 0;
		}
		grid[row][col] = 2;

		int maxArea = 0;
		maxArea += (maxArea, dfs(grid, row, col + 1));
		maxArea += (maxArea, dfs(grid, row, col - 1));
		maxArea += (maxArea, dfs(grid, row + 1, col));
		maxArea += (maxArea, dfs(grid, row - 1, col));

		return 1 + maxArea;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<vector<int>> v{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}};
	return a.maxAreaOfIsland(v);
}
