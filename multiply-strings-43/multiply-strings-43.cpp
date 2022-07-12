#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

#include <cstdlib>

using namespace std;
class Solution
{
public:
	string multiply(string num1, string num2)
	{
		if (num1 == "0" || num2 == "0")
			return "0";
		string result = "0";
		string max = num1.size() > num2.size() ? num1 : num2;
		string min = num1.size() <= num2.size() ? num1 : num2;
		int minSize = min.size();
		int maxSize = max.size();
		// I want to call the bigAdd procedure as little times as possible
		// That means I want to multiply by adding the bigger number the smaller number amount of times
		// Multiply by the following procedure: Multiply a and b by adding a, b times.
		// Let b be represents as b0b1b2b3b4b5 where each bn is the value of a digit, then
		// we first add a b0 times, then we add a (b1 * 10) times, then we add a (b2 * 100) times...

		string digitPadding = "";
		for (int digitIndex = 0; digitIndex < minSize; digitIndex++, digitPadding += "0")
		{
			int digitValue = min[minSize - digitIndex - 1] - '0';

			for (int i = 0; i < (int)digitValue; i++)
				result = bigAdd(result, max + digitPadding);
		}
		return result;
	}
	string bigAdd(string num1, string num2)
	{
		if (num1 == "0")
			return num2;
		if (num2 == "0")
			return num1;
		string result = "";
		string max = num1.size() > num2.size() ? num1 : num2;
		string min = num1.size() <= num2.size() ? num1 : num2;

		int minSize = min.size();
		int maxSize = max.size();
		// we can add any 9 digit numbers together since INT_MAX has 10 digits
		// starting from the lowest order digits, we add 9 digits together at a time
		// and grow the result string leftwards.
		bool overflowFlag = 0;
		for (int i = 0; i < minSize / 9; i++)
		{
			int minChunk = stoi(min.substr(minSize - (i + 1) * 9, 9));
			int maxChunk = stoi(max.substr(maxSize - (i + 1) * 9, 9));
			int sum = minChunk + maxChunk + overflowFlag;
			overflowFlag = 0;
			string sumstr = to_string(sum);
			result = sumstr + result;
			if (sumstr.size() < 9)
			{
				// There must have been some truncated 0 due to int +, add them back to string
				// add back zeroes so that sumstr is length 9
				for (int i = 0; i < 9 - sumstr.size(); i++)
					result = "0" + result;
			}
			else if (sumstr.size() == 10)
			{
				overflowFlag = 1; // positive overflow occured
				result = result.substr(1);
			}
		}
		// we now add the smaller string's residue (len 0 to 9) with the corresponding part in the longer string
		int residueLength = minSize % 9;
		if (residueLength == 0 && minSize == maxSize) // no leftover at all
		{
			if (overflowFlag)
				result = "1" + result;
			return result;
		}
		else if (residueLength == 0) // no min residual, but max does have residue
		{
			return to_string(stoi(max.substr(0, maxSize - minSize)) + overflowFlag) + result;
		}
		else if (minSize == maxSize) // yes residual, but they have same lengths
		{
			// add together along with overflow
			string minResidue, maxResidue;
			minResidue = min.substr(0, residueLength);
			maxResidue = max.substr(maxSize - minSize, residueLength);
			int residue = stoi(minResidue) + stoi(maxResidue) + overflowFlag;
			string residueSumstr = to_string(residue);
			return residueSumstr + result;
		}
		else // yes residual, and, max has more leftover after matching min's residual
		{
			string minResidue, maxResidue;
			minResidue = min.substr(0, residueLength);
			maxResidue = max.substr(maxSize - minSize, residueLength);

			int residue = stoi(minResidue) + stoi(maxResidue) + overflowFlag;
			string residueSumstr = to_string(residue);
			overflowFlag = 0;
			if (residueSumstr.size() == residueLength + 1)
			{
				residueSumstr = residueSumstr.substr(1);
				string maxLeftOver = bigAdd(max.substr(0, maxSize - minSize), "1"); // last number adds 1
				return maxLeftOver + residueSumstr + result;
			}
			else
			{ // no overflow, simply add max leftover, residual, and result together
				return max.substr(0, maxSize - minSize) + residueSumstr + result;
			}
		}
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	// cout << a.multiply("0", "0") << " == 0?" << endl;
	// cout << a.bigAdd("218868959400", "60594950000") << endl;

	// 95500000000
	//  4500000000
	cout << a.multiply("498828660196", "840477629533"); // carry bit from main blocks overflows residual sum which overflows max left over

	// int tests = 10000000;
	// int max = (INT_MAX / 2);
	// int min = 0;
	// for (int i = 0; i < tests; i++)
	// {
	// 	int b = rand() % (max - min + 1) + min;
	// 	int c = rand() % (max - min + 1) + min;
	// 	int final = b + c;
	// 	if ((final) != stoi(a.bigAdd(to_string(b), to_string(c))))
	// 	{
	// 		cout << "The following bigAdd did not work: " << b << ", " << c << "; it's supposed to be: " << final << ", but instead received " << a.bigAdd(to_string(b), to_string(c)) << endl;
	// 	}
	// }
	// for (int i = 0; i < tests; i++)
	// {
	// 	int b = rand() % (max - min + 1) + min;
	// 	int c = rand() % (max - min + 1) + min;
	// 	int final = b * c;
	// 	if ((final) != stoi(a.multiply(to_string(b), to_string(c))))
	// 	{
	// 		cout << "The following multiply did not work: " << b << ", " << c << "; it's supposed to be: " << final << ", but instead received " << a.multiply(to_string(b), to_string(c)) << endl;
	// 	}
	// }

	return 0;
}
