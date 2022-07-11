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
	ListNode *removeNthFromEnd(ListNode *head, int n)
	{
		// pointer fast starts at nth node from head
		// pointer slow starts at head (slow and fast are n steps apart)
		// Move pointer fast until last node, since slow and fast are n steps apart, slow points at (n+1)th node from head
		ListNode *fast = head, *slow = head;
		for (int i = 0; i < n; i++)
			fast = fast->next;

		if (!fast)
		{
			return head->next;
		}

		while (fast->next)
		{
			fast = fast->next;
			slow = slow->next;
		}

		slow->next = slow->next->next;

		return head;
	}
};

int main(int argc, char *argv[])
{
	Solution fast;
	return 0;
}
