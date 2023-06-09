// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let n = letters.len();

        if target as u32 >= letters[n - 1] as u32 {
            return letters[0];
        }
        
        let mut left = 0;
        let mut right = (n - 1) as i32;
        let target = target as u32;
        
        while left <= right {
            let mid = left + (right - left) / 2;
            if letters[mid as usize] as u32 > target {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return letters[left as usize];
    }
}
