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
    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
    {
        int prevColor = image[sr][sc];
        if (prevColor == newColor)
        {
            return image;
        }

        dfs(image, sr, sc, newColor, prevColor);
        return image;
    }

    void dfs(vector<vector<int>> &image, int row, int col, int newColor, int prevColor)
    {

        if (row < 0 or col < 0 or row > image.size() - 1 or col > image[0].size() - 1)
        {
            return;
        }

        if (image[row][col] != prevColor)
        {
            return;
        }

        image[row][col] = newColor;
        dfs(image, row, col + 1, newColor, prevColor);
        dfs(image, row, col - 1, newColor, prevColor);
        dfs(image, row + 1, col, newColor, prevColor);
        dfs(image, row - 1, col, newColor, prevColor);
    }
};

int main(int argc, char *argv[])
{
    Solution a;
    vector<vector<int>> b{{0, 0, 0}, {0, 1, 1}};

    a.floodFill(b, 1, 1, 1);
    return 0;
}
