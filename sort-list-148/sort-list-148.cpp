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
	ListNode *mid(ListNode *head)
	{
		ListNode *slow = head, *fast = head;
		while (fast != nullptr && fast->next != nullptr && fast->next->next != nullptr)
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		return slow;
	}
	// Merge two sorted lists into one sorted list
	ListNode *merge(ListNode *left, ListNode *right)
	{
		if (left == nullptr)
			return right;
		if (right == nullptr)
			return left;
		if (left->val <= right->val)
		{
			left->next = merge(left->next, right);
			return left;
		}
		else
		{
			right->next = merge(left, right->next);
			return right;
		}
	}
	ListNode *sortList(ListNode *head)
	{
		if (head == nullptr || head->next == nullptr)
			return head;
		ListNode *middle = mid(head);
		ListNode *middleNext = middle->next;
		middle->next = nullptr;
		return merge(sortList(head), sortList(middleNext));
	}
	void mergeSort(int arr[], int start, int end)
	{
		if (end <= start)
			return;
		int mid = start + (end - start) / 2;
		mergeSort(arr, start, mid);
		mergeSort(arr, mid + 1, end);
		merge(arr, start, mid, end);
	}
	void merge(int arr[], int start, int mid, int end)
	{
		int leftArrInd = start, rightArrInd = mid + 1;
		int temp[end - start + 1];
		int tempInd = 0;
		for (int i = 0; leftArrInd <= mid && rightArrInd <= end; i++)
		{
			if (arr[leftArrInd] <= arr[rightArrInd])
			{
				temp[i] = arr[leftArrInd];
				leftArrInd++;
				tempInd++;
			}
			else
			{
				temp[i] = arr[rightArrInd];
				rightArrInd++;
				tempInd++;
			}
		}
		for (int i = 0; leftArrInd <= mid; i++)
		{
			temp[tempInd] = arr[leftArrInd];
			leftArrInd++;
			tempInd++;
		}
		for (int i = 0; rightArrInd <= end; i++)
		{
			temp[tempInd] = arr[rightArrInd];
			rightArrInd++;
			tempInd++;
		}
		for (int i = 0; i <= end - start; i++)
		{
			arr[start + i] = temp[i];
		}
	}
};
void print(ListNode *head)
{
	for (ListNode *iter = head; iter != nullptr; iter = iter->next)
	{
		cout << iter->val;
	}
	cout << endl;
}

ListNode *createLL(vector<int> v)
{
	ListNode *head = new ListNode(v[0]);
	ListNode *iter = head;
	for (int i = 1; i < v.size(); i++, iter = iter->next)
		iter->next = new ListNode(v[i]);
	return head;
}

int main(int argc, char *argv[])
{
	Solution a;
	ListNode *test = createLL({3, 1, 6, 1, 2,3, 4, 7});
	ListNode *b = a.sortList(test);
	print(b);

	return 0;
}
