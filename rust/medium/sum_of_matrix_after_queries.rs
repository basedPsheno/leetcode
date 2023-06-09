// https://leetcode.com/problems/sum-of-matrix-after-queries/

impl Solution {
    pub fn matrix_sum_queries(n: i32, queries: Vec<Vec<i32>>) -> i64 {
        let mut seen_rows = 0;
        let mut seen_cols = 0;
        let mut sum_matrix: i64 = 0;

        let mut rows = vec![true; n as usize];
        let mut cols = vec![true; n as usize];

        for query in queries.iter().rev() {
            if query[0] == 0 && rows[query[1] as usize] {
                seen_rows += 1;
                rows[query[1] as usize] = false;
                sum_matrix += ((n - seen_cols) * query[2]) as i64;
            }
            if query[0] == 1 && cols[query[1] as usize] {
                seen_cols += 1;
                cols[query[1] as usize] = false;
                sum_matrix += ((n - seen_rows) * query[2]) as i64;
            }
        }

        sum_matrix
    }
}
