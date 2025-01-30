use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::time::{SystemTime, UNIX_EPOCH};

fn run_write_loop_for_file() {
    let path = Path::new("bin/expt3.txt");
    let mut file = match File::create(&path) {
        Err(why) => panic!("couldn't create {}: {}", path.display(), why),
        Ok(file) => file,
    };
    let mut result = String::new();
    for i in 1..1000000 {
        let log_line = format!("test{}\n", i);
        result.push_str(&log_line);
    }
    file.write(result.as_bytes()).expect("TODO: panic message");
    file.sync_all().unwrap();
}

fn main() {
    let start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    run_write_loop_for_file();
    let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    println!("Time taken for direct file writes = {}", end.as_millis()-start.as_millis());
}