// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len() as i32, grid[0].len() as i32);
        let (mut i, mut j) = (m - 1, 0);
        let mut count = 0;

        while i > -1 && j < n {
            if grid[i as usize][j as usize] < 0 {
                count += n - j;
                i -= 1;
            } else {
                j += 1;
            }
        }

        count
    }
}
