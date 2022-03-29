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
	bool exist(vector<vector<char>> &board, string word)
	{
		for (int row = 0; row < board.size(); row++)
		{
			for (int col = 0; col < board[0].size(); col++)
			{
				if (existRecur(board, word, row, col, 0))
					return true;
			}
		}
		return false;
	}

	bool existRecur(vector<vector<char>> &board, string &word, int row, int col, int index)
	{

		if (index == word.size())
			return true;

		if (row < 0 || col < 0 || row >= board.size() || col >= board[0].size())
			return false;

		if (board[row][col] != word[index])
			return false;

		if (board[row][col] = '.')
			return false;
		char temp = board[row][col];
		board[row][col] = '.';

		return existRecur(board, word, row + 1, col, index + 1, isVisited) ||
			   existRecur(board, word, row - 1, col, index + 1, isVisited) ||
			   existRecur(board, word, row, col + 1, index + 1, isVisited) ||
			   existRecur(board, word, row, col - 1, index + 1, isVisited);
		board[row][col] = temp;
		return false;
	}
};

int main(int argc, char *argv[])
{
	Solution a;

	vector<vector<char>> board = {{'A', 'B', 'C', 'E'},
								  {'S', 'F', 'C', 'S'},
								  {'A', 'D', 'E', 'E'}};

	printf("%i\n", a.exist(board, "SEE"));
	return 0;
}
