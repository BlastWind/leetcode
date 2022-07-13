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
	// O(n) running time and O(1) space by going to mid of linked list, reversing mid, and comparing head to mid
	bool isPalindrome(ListNode *head)
	{
		// Interesting observation: To get to the 1/n th node in the link list, make fast pointer travel at n speed
		// while make slow ptr travel at 1 speed. When fast pointer goes out of bounds, slow ptr points at 1/n th
		ListNode *slow = head, *fast = head;
		while (fast != nullptr && fast->next != nullptr)
		{
			fast = fast->next->next;
			slow = slow->next;
		}
		// COMMENTED OUT IS A NAIVE WAY OF OBTAINING MID
		// int llLength = 0;
		// for (ListNode *iter = head; iter != nullptr; iter = iter->next)
		// 	llLength++;
		// ListNode *mid = head;
		// for (int i = 0; i < llLength / 2; i++)
		// 	mid = mid->next;
		// reverse mid, prev will hold the head of the reversed string
		ListNode *mid = slow, *prev = nullptr, *cur = mid;
		while (cur != nullptr)
		{
			ListNode *temp = cur->next;
			cur->next = prev;
			prev = cur;
			cur = temp;
		}
		mid = prev;
		// if head to mid is the same as reversed mid to end, palindrome it is
		for (; mid != nullptr; mid = mid->next, head = head->next)
			if (head->val != mid->val)
				return false;
		return true;
	}
	// // naive solution: convert LinkedList to array and do usual palindrome comparison
	// bool isPalindrome(ListNode* head) {
	// 	vector<int> arr;
	// 	while(head != nullptr){
	// 		arr.push_back(head->val);
	// 		head = head->next;
	// 	}
	// 	// for even arr size 10, this goes from 0 to 4
	// 	// and we compare
	// 	for(int i = 0; i < arr.size() / 2; i++){
	// 		if(arr[i] != arr[arr.size() - i - i]) return false;
	// 	}
	// 	return true;
	// }
};

int main(int argc, char *argv[])
{
	Solution a;
	a.isPalindrome(new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1)))));
	return 0;
}
