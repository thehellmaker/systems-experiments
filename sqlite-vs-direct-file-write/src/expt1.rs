use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::time::{SystemTime, UNIX_EPOCH};
use rusqlite::{params, Connection};

fn run_write_loop_for_sqlite() {
    let mut connection = Connection::open("bin/expt1.db").unwrap();
    connection.execute_batch("
            PRAGMA journal_mode = WAL;
            PRAGMA synchronous = NORMAL;
    ").expect("PRAGMA");

    connection.execute(
        "CREATE TABLE IF NOT EXISTS log(logline text)",
        []).expect("TODO: panic message"
    );

    let transaction = connection.transaction().unwrap();

    {
        let mut statement = transaction.prepare_cached("INSERT INTO log (logline) VALUES ($1)").unwrap();
        for i in 1..1000000 {
            let log_line = format!("test{}", i);
            statement.execute(params![log_line]).unwrap();
        }
    }
    transaction.commit().unwrap();
}

fn run_write_loop_for_file() {
    let path = Path::new("bin/expt1.txt");
    let mut file = match File::create(&path) {
        Err(why) => panic!("couldn't create {}: {}", path.display(), why),
        Ok(file) => file,
    };
    for i in 1..1000000 {
        let log_line = format!("test{}\n", i);
        file.write(log_line.as_bytes()).expect("TODO: panic message");
    }
    file.sync_all().unwrap();
}

fn main() {
    {
        let start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
        run_write_loop_for_sqlite();
        let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
        println!("Time Taken For SQLite = {}", end.as_millis()-start.as_millis());
    }
    {
        let start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
        run_write_loop_for_file();
        let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
        println!("Time Taken For direct file writes = {}", end.as_millis()-start.as_millis());
    }
}