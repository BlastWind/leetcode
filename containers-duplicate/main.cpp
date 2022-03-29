#include <string>
#include <vector>
#include <stdlib.h>
#include <unordered_map>
using namespace std;

class Solution
{
public:
	bool containsDuplicate(vector<int> &nums)
	{
		unordered_map<int, int> umap;
		for (int i = 0; i < nums.size(); i++)
		{
			if (umap.find(nums[i]) != umap.end())
				return true;
			umap[nums[i]] = 1;
		}

		return false;
	}
};

int main()
{
	Solution a;
	vector<int> nums = {1, 2, 3, 4};
	a.containsDuplicate(nums);
}