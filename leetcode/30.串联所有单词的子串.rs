/*
 * @lc app=leetcode.cn id=30 lang=rust
 *
 * [30] 串联所有单词的子串
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        let mut result = Vec::new();
        if words.is_empty() {
            return result;
        }
        
        let word_len = words[0].len();
        let total_words = words.len();
        let total_len = word_len * total_words;
        let s_len = s.len();
        
        if s_len < total_len {
            return result;
        }
        
        let mut target_map: HashMap<&str, usize> = HashMap::new();
        for word in &words {
            *target_map.entry(word.as_str()).or_insert(0) += 1;
        }
        
        for i in 0..word_len {
            let mut current_map = HashMap::new();
            let mut left = i;
            let mut count = 0;
            
            for j in (i..=s_len - word_len).step_by(word_len) {
                let current_word = &s[j..j + word_len];
                
                if !target_map.contains_key(current_word) {
                    current_map.clear();
                    count = 0;
                    left = j + word_len;
                    continue;
                }
                
                *current_map.entry(current_word).or_insert(0) += 1;
                count += 1;
                
                while *current_map.get(current_word).unwrap() > *target_map.get(current_word).unwrap() {
                    let left_word = &s[left..left + word_len];
                    *current_map.get_mut(left_word).unwrap() -= 1;
                    count -= 1;
                    left += word_len;
                }
                
                if count == total_words {
                    result.push(left as i32);
                    let left_word = &s[left..left + word_len];
                    *current_map.get_mut(left_word).unwrap() -= 1;
                    count -= 1;
                    left += word_len;
                }
            }
        }
        
        result
    }
}
// @lc code=end

