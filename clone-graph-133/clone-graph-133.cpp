/*
Key idea: When a complicated node is cloned, add it to an unordered map.
The reason to do so is that if 1->2->3->1, then 1 is 2's and 3's neighbor. Therefore, no need to
clone 1 from scratch, in fact, doing so will be infinite.
And there is no reason to clone them from scratch twice.
*/
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
		unordered_map<Node *, Node *> umap;

		return dfs(node, umap);
	}
	Node *dfs(Node *orig, unordered_map<Node *, Node *> &umap)
	{
		/* dfs only Runs if the orig has been mapped */
		Node *clone = new Node(orig->val);
		umap[orig] = clone; // take over map

		for (auto it : orig->neighbors)
		{
			// if the neighbor already is constructed (created in umap), directly push it into orig->neighbors
			if (umap.find(it) != umap.end())
			{
				clone->neighbors.push_back(umap[it]);
			}
			else
			{
				clone->neighbors.push_back(dfs(it, umap));
			}
		}

		return clone;
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
