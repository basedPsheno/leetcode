// https://leetcode.com/problems/design-underground-system/ 

use std::collections::HashMap;

#[derive(Default)]
struct UndergroundSystem {
    journey: HashMap<i32, (String, i32)>,
    history: HashMap<(String, String), (i32, u32)>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl UndergroundSystem {

    fn new() -> Self {
        Default::default()
    }
    
    fn check_in(&mut self, id: i32, start_station: String, start_time: i32) {
        self.journey.insert(id, (start_station, start_time));
    }
    
    fn check_out(&mut self, id: i32, end_station: String, end_time: i32) {
        if let Some((start_station, start_time)) = self.journey.get(&id) {
            let travel = self
                .history
                .entry((start_station.clone(), end_station))
                .or_default();
            travel.0 += end_time - start_time;
            travel.1 += 1
        }
    }
    
    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        if let Some(&(total_time, count)) = self.history.get(&(start_station, end_station)) {
            return f64::from(total_time) / count as f64
        }
        unreachable!()
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */
