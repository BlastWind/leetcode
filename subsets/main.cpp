#include <iostream>
#include <string>

using namespace std;

void subsetCompute(string cur, string rest)
{
	if (rest.length() == 0)
	{
		printf("%s\n", cur.c_str()); // print completely built up string
		return;
	}
	// add the letter AND not add the letter, visualize the recursive call tree to make sense of this
	subsetCompute(cur + rest[0], rest.substr(1));
	subsetCompute(cur, rest.substr(1));
}

int main()
{
	subsetCompute("", "asdf");
}