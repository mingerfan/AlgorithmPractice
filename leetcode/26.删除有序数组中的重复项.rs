/*
 * @lc app=leetcode.cn id=26 lang=rust
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let mut pivot = i32::MAX;
        let mut cnt = 0;
        while right < nums.len() {
            if pivot != nums[right] {
                cnt += 1;
                pivot = nums[right];
                nums[left] = pivot;
                left += 1;
            } else {
                right += 1;
            }
        }
        cnt
    }
}
// @lc code=end

