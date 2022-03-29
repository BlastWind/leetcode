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
				vector<vector<bool>> isVisited(board.size(), vector<bool>(board[0].size(), 0));

				if (recurIfConditionsMet(board, word, row, col, 0, isVisited))
					return true;
			}
		}
		return false;
	}

	bool existRecur(vector<vector<char>> &board, string word, int row, int col, int index, vector<vector<bool>> &isVisited)
	{
		if (index >= word.length() - 1)
		{
			if (board[row][col] == word[index])
			{
				return true;
			}
		}

		isVisited[row][col] = true;

		if (recurIfConditionsMet(board, word, row, col - 1, index + 1, isVisited))
			return true;
		if (recurIfConditionsMet(board, word, row, col + 1, index + 1, isVisited))
			return true;
		if (recurIfConditionsMet(board, word, row + 1, col, index + 1, isVisited))
			return true;
		if (recurIfConditionsMet(board, word, row - 1, col, index + 1, isVisited))
			return true;
		isVisited[row][col] = false;
		return false;
	}

	bool recurIfConditionsMet(vector<vector<char>> &board, string word, int row, int col, int index, vector<vector<bool>> &isVisited)
	{
		if (row < 0 || row > board.size() - 1 || col < 0 || col > board[0].size() - 1)
			return false;
		if (isVisited[row][col] == true)
			return false;
		if (board[row][col] == word[index])
			return existRecur(board, word, row, col, index, isVisited);
		return false;
	}
};