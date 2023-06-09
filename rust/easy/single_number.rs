// https://leetcode.com/problems/single-number/

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        nums.iter().fold(0, |ans, num| ans ^ num)
    }
}
