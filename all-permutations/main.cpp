#include <iostream>
#include <string>

using namespace std;

void permutationCompute(string cur, string rest)
{
	if (rest.length() == 0)
	{
		printf("%s\n", cur.c_str()); // print completely built up string
		return;
	}
	for (int i = 0; i < rest.length(); i++) // deceptive i recursive calls!
	{
		permutationCompute(cur + rest[i], rest.substr(0, i) + rest.substr(i + 1)); // build up string one letter at a time, selected from the 'rest' pool
	}
}

int main()
{
	permutationCompute("", "asdf");
}