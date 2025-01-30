use std::{thread, time};
use std::time::{SystemTime, UNIX_EPOCH};
use rusqlite::{params, Connection};

fn run_write_loop_for_sqlite() {
    let mut connection = Connection::open("bin/expt2.db").unwrap();
    connection.execute_batch("
            PRAGMA journal_mode = WAL;
            PRAGMA synchronous = EXTRA;
        ").expect("PRAGMA");

    connection.execute(
        "CREATE TABLE IF NOT EXISTS log(logline text)",
        []).expect("TODO: panic message");

    let transaction = connection.transaction().unwrap();

    {
        let mut statement = transaction.prepare_cached("INSERT INTO log (logline) VALUES ($1)").unwrap();

        let mut start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
        for i in 1..10000000 {
            let log_line = format!("test{}", i);
            statement.execute(params![log_line]).unwrap();

            if i % 1000000 == 0 {
                let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
                println!("100k Write Time Taken = {}", end.as_millis()-start.as_millis());
                println!("Sleep Start");
                thread::sleep(time::Duration::from_millis(1000*20));
                println!("Sleep End");
                start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
            }
        }
    }
    transaction.commit().unwrap();
}

fn main() {
    run_write_loop_for_sqlite();
}