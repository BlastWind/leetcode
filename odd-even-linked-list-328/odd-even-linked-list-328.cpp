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
	// optimzed version, simply think of two linked lists starting one space separting using each other's immediate next value
	ListNode *oddEvenList(ListNode *head)
	{
		if (head == nullptr || head->next == nullptr)
			return head;
		ListNode *odd = head, *even = head->next, *evenHead = even;
		while (even != nullptr && even->next != nullptr) // optimization 1) Even is tail and so can be used to check exit conditions
		{
			// optimization 2) Instead of doing almost
			/*
				while(C) {
					if odd iteration do x update condition
					if even iterations do y update condition
				}
			*/
			// just do similar to: 
			/*
				while(C){
					do x 
					do y 
					update condition
				}
			*/
			odd->next = even->next;
			odd = odd->next;
			even->next = odd -> next;
			even = even->next;
		}
		even->next = nullptr;
		odd->next = evenHead;
		return head; 
	}
	// ListNode* oddEvenList(ListNode* head) {
	//     if(head == nullptr || head -> next == nullptr) return head;
	//     ListNode* odd = head, *even = head->next, *oddHead = odd, *evenHead = even;
	//     bool oddFlag = 1;
	//     head = head -> next -> next;
	//     while(head != nullptr){
	//         if(oddFlag) {
	//             odd -> next = head;
	//             odd = odd -> next;
	//         }else {
	//             even -> next = head;
	//             even = even -> next;
	//         }
	//         oddFlag = !oddFlag;
	//         head = head -> next;
	//     }
	// 	even -> next = nullptr;
	//     odd -> next = evenHead;
	//     return oddHead;
	// }
};

int main(int argc, char *argv[])
{
	ListNode *head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
	Solution a;
	a.oddEvenList(head);
	return 0;
}
