// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut k = 1;
        let mut _j = 1;

        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                nums[_j] = nums[i];
                _j += 1;
                k += 1;
            }
        }

        k
    }
}
