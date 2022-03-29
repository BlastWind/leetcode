#include <string>
#include <vector>
#include <stdlib.h>
#include <unordered_map>
using namespace std;

class Solution
{
public:
	vector<int> productExceptSelf(vector<int> &nums)
	{
		vector<int> prefixes = {1};
		vector<int> suffixes = {1};

		for (int i = 1; i < nums.size(); i++)
		{
			prefixes.push_back(prefixes[i - 1] * nums[i - 1]);
			suffixes.push_back(suffixes[i - 1] * nums[nums.size() - i]);
		}

		vector<int> products;
		for (int i = 0; i < nums.size(); i++)
		{
			products.push_back(prefixes[i] * suffixes[nums.size() - 1 - i]);
		}

		return products;
	}
};

int main(int argc, char *argv[])
{
	Solution a;
	vector<int> nums;
	for (int i = 0; i < argc; i++)
	{
		nums.push_back(strtol(argv[i], NULL, 10));
	}
	nums = a.productExceptSelf(nums);
	for (auto i : nums)
	{
		printf("%d ", i);
	}
}