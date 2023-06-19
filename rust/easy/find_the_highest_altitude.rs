// https://leetcode.com/problems/find-the-highest-altitude/

use std::cmp::max;

impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut highest_alt = 0;
        let mut cur_alt = 0;

        for alt in gain.iter() {
            cur_alt += alt;
            highest_alt = max(highest_alt, cur_alt);
        }

        highest_alt
    }
}
