#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        return recur(nullptr, head);
    }
	ListNode* recur(ListNode* prev, ListNode* cur){
		if(cur == nullptr) return prev; 
		ListNode * temp = cur -> next; 
		cur -> next = prev; 
		return recur(cur, temp);
	}
};

int main(int argc, char *argv[])
{
	ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4)))); 
	Solution a;
	a.reverseList(head); 
	return 0;
}
