/*
 * @lc app=leetcode.cn id=80 lang=rust
 *
 * [80] 删除有序数组中的重复项 II
 */

// @lc code=start
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let mut pivot = i32::MAX;
        let mut pivot_cnt = 0;
        while right < nums.len() {
            if pivot == nums[right] {
                pivot_cnt += 1;
            } else {
                pivot = nums[right];
                pivot_cnt = 0;
            }
            if pivot_cnt < 2 {
                nums[left] = nums[right];
                left += 1;
                right += 1;
            } else {
                right += 1;
            }
        }
        left as i32
    }
}
// @lc code=end

