#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

using namespace std;

class Node
{
public:
	int val;
	vector<Node *> neighbors;
	Node()
	{
		val = 0;
		neighbors = vector<Node *>();
	}
	Node(int _val)
	{
		val = _val;
		neighbors = vector<Node *>();
	}
	Node(int _val, vector<Node *> _neighbors)
	{
		val = _val;
		neighbors = _neighbors;
	}
};

class Solution
{
public:
	Node *cloneGraph(Node *node)
	{

		Node firstClone(node->val);
		dfs(node, &firstClone);
		return &firstClone;
	}
	void dfs(Node *original, Node *clone)
	{
		for (auto neighbor : original->neighbors)
		{
			Node neighborClone(neighbor->val);
			clone->neighbors.push_back(&neighborClone);
			dfs(neighbor, &neighborClone);
		}
	}
};

int main(int argc, char *argv[])
{
	Node a{7};
	Node b{8};
	a.neighbors.push_back(&b);
	Solution c;
	Node *ay = c.cloneGraph(&a);
	return 0;
}
