/*
 * @lc app=leetcode.cn id=27 lang=rust
 *
 * [27] 移除元素
 */

// @lc code=start
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut cnt = 0;
        let mut left = 0;
        let mut right = 0;
        loop {
            while left < nums.len() && nums[left] != val {
                left += 1;
                cnt += 1;
            }
            if right < left {
                right = left + 1;
            }
            while right < nums.len() && nums[right] == val {
                right += 1;
            }
            if right >= nums.len() {
                break;
            }
            let temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
        }
        cnt
    }
}
// @lc code=end

