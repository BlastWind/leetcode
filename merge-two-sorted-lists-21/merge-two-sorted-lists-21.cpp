#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

using namespace std;

struct ListNode
{
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
	ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
	{

		if (!list2)
			return list1;
		if (!list1)
			return list2;
		if (list1->val <= list2->val)
		{
			list1->next = mergeTwoLists(list1->next, list2); // reuse list1 elements instead of having to invoke new ListNode()
			return list1;
		}
		list2->next = mergeTwoLists(list1, list2->next); // reuse list2 elements instead of having to invoke new ListNode()
		return list2;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	return 0;
}
