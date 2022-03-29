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
		for (int i = 0; i < board.size(); i++)
		{
			for (int j = 0; j < board[0].size(); j++)
			{
				if (dfs(board, word, 0, i, j))
					return true;
			}
		}
		return false;
	}

	bool dfs(vector<vector<char>> &board, string word, int cur, int row, int col)
	{
		// END CONDITION
		// Perhaps, ending is not immediately true, so do a condition check again
		if (cur > word.length() - 1)
			return true;

		if (row < 0 || col < 0 || row > board.size() - 1 || col > board[0].size() - 1)
		{
			return false;
		}

		if (board[row][col] == '~')
		{
			return false;
		}

		if (board[row][col] != word[cur])
		{
			return false;
		}

		char temp = board[row][col];
		board[row][col] = '~'; // isVisited

		// FOR EACH DECISION
		// FORWARD TRACK
		// IF PERFORM DECISION returns true, return true
		// BACK TRACK
		//

		if (dfs(board, word, cur + 1, row + 1, col) || dfs(board, word, cur + 1, row - 1, col) || dfs(board, word, cur + 1, row, col + 1) || dfs(board, word, cur + 1, row, col - 1))
		{
			return true;
		}

		board[row][col] = temp;
		return false;
	}
};

int main()
{
	Solution a;
	vector<vector<char>> b{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
	a.exist(b, "SEE");
}