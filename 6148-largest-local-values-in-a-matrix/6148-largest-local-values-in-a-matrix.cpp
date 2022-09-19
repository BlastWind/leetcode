vector<vector<int>> largestLocal(vector<vector<int>> &g)
{
	vector<vector<int>> res(grid.length - 2 - 2, vector<int>(grid.length - 2 - 2));
	for (int i = 0; i < grid.length - 2 - 2; ++i)
		for (int j = 0; j < grid.length - 2 - 2; ++j)
			for (int ii = i; ii < i + 3; ++ii)
				for (int jj = j; jj < j + 3; ++jj)
					res[i][j] = max(res[i][j], g[ii][jj]);
	return res;
}