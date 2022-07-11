#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution
{
public:
	bool isHappy(int n)
	{
		unordered_set<int> set;
		do
		{
			int sumOfSquares = 0;
			while (n != 0)
			{
				int lowestDigit = n % 10;
				sumOfSquares += lowestDigit * lowestDigit;
				n /= 10;
			}
			if (sumOfSquares == 1)
				return true;
			if (set.find(sumOfSquares) != set.end())
				return false;
			set.emplace(sumOfSquares);
			n = sumOfSquares;
		} while (true);
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	int n = 19;
	cout << a.isHappy(n) << endl;
	return 0;
}
