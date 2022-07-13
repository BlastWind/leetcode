/**
 * In odd-even-linked-list-328, we split the linked list into 2 partitions, with each partition taking every other node
 * I extend this to a "every-nth-partition-linked-list" problem: I make n partitions, each ith partition starts from position i and consumes every nth node starting from the i
 */

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
	ListNode *everyNthList(ListNode *head, int n) // maybe not the best name, we'll get better
	{
		if (n == 1)
			return head;
		ListNode *iter = head;
		vector<pair<ListNode *, ListNode *>> v; // pair.first = ptr used to iterate a partition (denotes the current end of the partition), pair.second = root of the partition
		for (int i = 0; i < n; i++, iter = iter->next)
		{
			if (iter == nullptr)
				return head;
			v.push_back(make_pair(iter, iter));
		}
		while (true) // while true along with goto, the hemlock or antidote to modern day programming?
		{
			// each partition -> next  = prev partition -> next
			// for example, if I am on the 2nd partition out of the 5 partitions, I want the next entry of the 2nd partition be what follows after the end of the 1st partition
			// for example, if I am on the 1st partition out of the 4 partitions, I want the next entry of the 1st partition be what follows after the end of the 4th partition
			for (int i = 0; i < n; i++)
			{
				auto prevPair = i == 0 ? v[n - 1] : v[i - 1];
				if (prevPair.first->next == nullptr) goto beginningOfTheEnd;
				v[i].first->next = prevPair.first->next;
				v[i].first = v[i].first->next;
			}
		}
	beginningOfTheEnd:
		auto firstPairEnd = v[0].first;
		for (int i = 1; i < n; i++) // Append the partitions after the 1st partition
		{
			firstPairEnd->next = v[i].second;
			firstPairEnd = v[i].first;
		}
		v[n - 1].first->next = nullptr; // Remove this, I dare you.
		return head; // head was never touched. 
	}
	ListNode* evenOddList(ListNode * head){
		return everyNthList(head, 2);
	}

};

void print(ListNode *head)
{
	for (; head != nullptr; head = head->next)
		cout << head->val << ", ";
	cout << endl;
}
ListNode *vectorToLinkedList(vector<int> &v, int index = 0)
{
	if (index == v.size())
		return nullptr;
	return new ListNode(v[index], vectorToLinkedList(v, index + 1));
}

int main(int argc, char *argv[])
{
	vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	ListNode *head = vectorToLinkedList(v);
	Solution a;
	print(a.everyNthList(head, 3));
	return 0;
}
