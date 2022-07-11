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
	string convert(string s, int numRows)
	{
		if (numRows == 1)
			return s;
		// naive O(n^2) space
		char zigzag[numRows][s.length()];
		memset(zigzag, 0, sizeof(zigzag));

		int row = 0, col = 0, isGoingVerically = 1;
		for (int i = 0; i < s.length(); i++)
		{
			// cout << s[i] << endl;
			zigzag[row][col] = s[i];

			if (row == numRows - 1)
			{
				// if cursor at zigzag "bottom"
				row -= 1;
				col += 1;
				isGoingVerically = 0;
				continue;
			}
			if (row == 0)
			{
				row += 1;
				isGoingVerically = 1;
				continue;
			}
			if (isGoingVerically)
			{
				row += 1;
			}
			else
			{
				row -= 1;
				col += 1;
			}
		}
		string a;
		cout << "size of zigzag: " << sizeof(zigzag) << "size of a zigzag row" << sizeof(zigzag[0]) << endl;
		cout << "size of zigzag[0]: " << sizeof(zigzag[0]) << "size of a zigzag[0][0]" << sizeof(zigzag[0][0]) << endl;
		for (int i = 0; i < sizeof(zigzag) / sizeof(zigzag[0]); i++)
		{
			for (int j = 0; j < sizeof(zigzag[0]) / sizeof(zigzag[0][0]); j++)
			{
				if (zigzag[i][j])
					a.push_back(zigzag[i][j]);
			}
		}
		return a;
	}
	string fastConvert(string s, int numRows)
	{
		if (numRows == 1)
			return s;
		// naive O(n^2) space
		string zigzag[numRows];

		int row = 0, col = 0, isGoingVerically = 1;

		int i = 0;
		while (s[i])
		{
			for (int a = 0; a < numRows; a++, i++)
				zigzag[a] += s[i];
			for (int a = numRows - 2; a > 0; a--, i++)
				zigzag[a] += s[i];
		}

		string a;
		for (int i = 0; i < numRows; i++)
			a += zigzag[i];
		return a;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	string s = "PAYPALISHIRING";
	cout << a.fastConvert(s, 3) << endl;
	return 0;
}
