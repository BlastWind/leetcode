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
	int numIslands(vector<vector<char>> &grid)
	{
		int totalCount = 0;
		for (int i = 0; i < grid.size(); i++)
		{
			for (int j = 0; j < grid[0].size(); j++)
			{
				bool isIsland = false;
				markVisited(grid, i, j, isIsland);
				if (isIsland)
				{
					totalCount++;
				}
			}
		}
		return totalCount;
	}

	void markVisited(vector<vector<char>> &grid, int row, int col, bool &isIsland)
	{
		if (row < 0 or col < 0 or row > grid.size() - 1 or col > grid.size() - 1)
		{
			return;
		}

		if (grid[row][col] == '1')
		{
			isIsland = true;
			grid[row][col] = '.';
			markVisited(grid, row, col + 1, isIsland);
			markVisited(grid, row, col - 1, isIsland);
			markVisited(grid, row + 1, col, isIsland);
			markVisited(grid, row - 1, col, isIsland);
		}
	}
};
int main(int argc, char *argv[])
{
	Solution a;
	vector<vector<char>> arr{{'1', '1', '1', '1', '0'}, {'1', '1', '0', '1', '0'}, {'1', '1', '0', '0', '0'}, {'0', '0', '0', '0', '0'}};
	a.numIslands(arr);
}