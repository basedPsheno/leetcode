// https://leetcode.com/problems/check-if-it-is-a-straight-line/

impl Solution {
    pub fn check_straight_line(coords: Vec<Vec<i32>>) -> bool {
        let [x0, y0] = [coords[0][0], coords[0][1]];
        let [x1, y1] = [coords[1][0], coords[1][1]];

        for i in 2..coords.len() {
            if (coords[i][0] - x0) * (y1 - y0) != (coords[i][1] - y0) * (x1 - x0) {
                return false;
            }
        }
        true
    }    
}


// use windows()
impl Solution {
    pub fn check_straight_line(coords: Vec<Vec<i32>>) -> bool {
        for p in coords.windows(3) {
            if ((p[1][1] - p[0][1]) * (p[2][0] - p[1][0]) != (p[2][1] - p[1][1]) * (p[1][0] - p[0][0])) {
                return false;
            }
        }
        true
    }
}
