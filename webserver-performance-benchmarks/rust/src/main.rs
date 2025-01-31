use dotenv::dotenv;
use rust_perf::server;

#[tokio::main(flavor="current_thread")]
async fn main() -> std::io::Result<()> {
    dotenv().ok(); // Reads the .env file
    server::http_server::start().await
}

