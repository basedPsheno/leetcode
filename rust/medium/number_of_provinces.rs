// https://leetcode.com/problems/number-of-provinces/

use std::collections::HashSet;

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let mut visited = HashSet::<usize>::new();
        let mut provinces: i32 = 0;

        for n in 0..is_connected.len() {
            if visited.contains(&n) {continue;}
            provinces += 1;
            DFS(n, &is_connected, &mut visited);
        }

        provinces        
    }
}

fn DFS(v: usize, is_connected: &Vec<Vec<i32>>, visited: &mut HashSet<usize>) {
    visited.insert(v);

    for u in 0..is_connected.len() {
        if is_connected[v][u] == 0 || visited.contains(&u) {continue;}
        DFS(u, is_connected, visited);
    }
}
