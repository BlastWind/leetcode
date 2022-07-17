/*
Incorrect but interestingly clean
The reason that this does not work is that from each node, a helper call targetting originalTarget is executed.
Obviously, then, there will be overlappings at a node directly equal to the originalTarget

To avoid overlappings, instead, I will, for each node, issue a helper call with only two branchings
This still encapsulates all the possibilities.
*/

#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

using namespace std;

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
	unordered_map<int, int> freq;
	int helper(TreeNode *root, long accumulated, int targetSum, unordered_map<int, int> &freq)
	{
		if (root == nullptr)
			return 0;
		int count = 0;
		accumulated += root->val;
		if (accumulated == targetSum)
			count++;
		if (freq.find(accumulated - targetSum) != freq.end())
			count += freq[accumulated - targetSum];
		freq[accumulated]++;
		int l = helper(root->left, accumulated, targetSum, freq);
		int r = helper(root->right, accumulated, targetSum, freq);
		freq[accumulated]--;
		return l + r + count;
	};
	int pathSum(TreeNode *root, int targetSum)
	{
		return helper(root, 0, targetSum, freq);
	}
};
int main(int argc, char *argv[])
{
	TreeNode *root = new TreeNode(10, new TreeNode(5, new TreeNode(3, new TreeNode(3), new TreeNode(-2)), new TreeNode(2, nullptr, new TreeNode(1))), new TreeNode(-3, nullptr, new TreeNode(11)));

	//[1,-2,-3,1,3,-2,null,-1]
	// TreeNode *root = new TreeNode(1, new TreeNode(-2, new TreeNode(1, new TreeNode(-1), nullptr), new TreeNode(3)), new TreeNode(-3, new TreeNode(-2), nullptr));
	Solution a;
	cout << a.pathSum(root, 3) << endl;
	return 0;
}
