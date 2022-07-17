/*
Incorrect but interestingly clean
The reason that this does not work is that from each node, a helper call targetting originalTarget is executed.
Obviously, then, there will be overlappings at a node directly equal to the originalTarget
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
	int pathSum(TreeNode *root, int targetSum) { return helper(root, targetSum, targetSum); }
	int helper(TreeNode *root, int targetSum, int originalTarget)
	{
		if (root == nullptr)
			return 0;
		// if (root->val == targetSum)
		// 	cout << root->val << endl;
		if (root->val == targetSum)
			return 1 + helper(root->left, targetSum - root->val, originalTarget) + helper(root->right, targetSum - root->val, originalTarget);
		int one = helper(root->left, targetSum - root->val, originalTarget);
		int two = helper(root->left, originalTarget, originalTarget);
		if (one || two)
			root->left = nullptr;
		int three = helper(root->right, targetSum - root->val, originalTarget);
		int four = helper(root->right, originalTarget, originalTarget);
		if (three || four)
			root->right = nullptr;

		return one + two + three + four;
	}
};
int main(int argc, char *argv[])
{
	// TreeNode *root = new TreeNode(10, new TreeNode(5, new TreeNode(3, new TreeNode(3), new TreeNode(-2)), new TreeNode(2, nullptr, new TreeNode(1))), new TreeNode(-3, nullptr, new TreeNode(11)));

	//[1,-2,-3,1,3,-2,null,-1]
	TreeNode *root = new TreeNode(1, new TreeNode(-2, new TreeNode(1, new TreeNode(-1), nullptr), new TreeNode(3)), new TreeNode(-3, new TreeNode(-2), nullptr));
	Solution a;
	cout << a.pathSum(root, 3) << endl;
	return 0;
}
