#include <iostream>
#include <vector>

using namespace::std;

// 使用dp，实际上可以使用贪心

/*
 * @lc app=leetcode.cn id=45 lang=cpp
 *
 * [45] 跳跃游戏 II
 */

// @lc code=start
class Solution {
public:
    int jump(vector<int>& nums) {
        auto dp = vector<int>(nums.size(), 0);
        for (auto i = 1; i < nums.size(); i++) {
            auto min = 10000000llU;
            for (auto j = 0; j < i; j++) {
                if (nums[j] + j >= i) {
                    min = dp[j] + 1 > min ? min : dp[j] + 1;
                } 
            }
            dp[i] = min;
        }
        return dp[nums.size() - 1];
    }
};
// @lc code=end

int main() {
    std::cout << "Hello";
    return 0;
}

