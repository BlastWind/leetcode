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
	vector<int> spiralOrder(vector<vector<int>> &matrix)
	{
		vector<int> v;
		smatF(matrix, v, 0, matrix.size() - 1, 0, matrix[0].size() - 1);
		return v;
	}

	void smatF(vector<vector<int>> &matrix, vector<int> &smat, int fromRow, int toRow, int fromCol, int toCol)
	{
		if (fromRow > toRow || fromCol > toCol)
			return;
		if (fromRow == toRow)
		{
			// add row to smat, no more branching (we've finished iterating)
			for (; fromCol <= toCol; fromCol++)
				smat.emplace_back(matrix[fromRow][fromCol]);
			return;
		}
		if (fromCol == toCol)
		{
			// add col to smat, no more branching
			for (; fromRow <= toRow; fromRow++)
				smat.emplace_back(matrix[fromRow][fromCol]);

			return;
		}
		// iterate around
		for (int i = fromCol; i <= toCol; i++) // iterates through columns
			smat.emplace_back(matrix[fromRow][i]);
		for (int i = fromRow + 1; i <= toRow; i++)
			smat.emplace_back(matrix[i][toCol]);
		for (int i = toCol - 1; i >= fromCol; i--) // iterates through columns
			smat.emplace_back(matrix[toRow][i]);
		for (int i = toRow - 1; i >= fromRow + 1; i--)
			smat.emplace_back(matrix[i][fromCol]);

		smatF(matrix, smat, fromRow + 1, toRow - 1, fromCol + 1, toCol - 1);
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<vector<int>> mat{
		{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
	vector<int> result = a.spiralOrder(mat);
	for (int i = 0; i < result.size(); i++)
		cout << result[i] << ", ";
	cout << endl;

	return 0;
}
