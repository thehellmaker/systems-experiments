
# Rust WebServer Performance**

A minimal Rust webserver built with the **Actix-web** framework backed by **tokio** runtime for analyzing performance. Exposes a simple API endpoint `/test`.

---

## **Getting Started**

### **Prerequisites**
- [Rust](https://www.rust-lang.org/tools/install) (version 1.70 or higher)
- [Cargo](https://doc.rust-lang.org/cargo/) (Rust's package manager)

### **Installation**
1. To build in dev mode for testing and development
    ```bash
    cargo run
    ```

2. Build and run the server in release mode for performance testing:
    ```bash
    cargo build
    ./target/release/rust-perf
    ```

  
2. The server will start on port `8080` with the log:
   ```txt
   Server running at http://127.0.0.1:8080
   ```

---

## **Endpoints**

### **CURL POST /test**
Parses a JSON payload, logs the `graphName` field, and returns the same JSON.
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"graphName":"xyz"}' \
  http://localhost:8080/test
```

**Example Response:**
```json
{
    "graphName": "xyz"
}
```

---

## **k6 Performance Test**
#### **Test Environment**: MacBook Pro 2018 x86 Model, 16GB RAM, 12 Cores
#### **Configuration**:
- 50 Virtual Users (VUs)
- 1-hour max duration

### **1 Million Requests**
```bash
k6 run -u 50 -i 1000000 --duration 1h --tag testname=million_request_test test.js
```

**Key Metrics**:
```
✓ Status 200: 100%
thehellmaker@thehellmakers-MacBook-Pro test % k6 run -u 50 -i 1000000 --duration 1h --tag testname=million_request_test test.js

         /\      Grafana   /‾‾/
    /\  /  \     |\  __   /  /
   /  \/    \    | |/ /  /   ‾‾\
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/

     execution: local
        script: test.js
        output: -

     scenarios: (100.00%) 1 scenario, 50 max VUs, 1h0m30s max duration (incl. graceful stop):
              * default: 1000000 iterations shared among 50 VUs (maxDuration: 1h0m0s, gracefulStop: 30s)


     ✓ Status is 200
     ✓ Correct JSON response

     checks.........................: 100.00% 2000000 out of 2000000
     data_received..................: 133 MB  4.3 MB/s
     data_sent......................: 162 MB  5.2 MB/s
     http_req_blocked...............: avg=7.58µs  min=1µs      med=3µs      max=41.76ms  p(90)=5µs    p(95)=6µs
     http_req_connecting............: avg=51ns    min=0s       med=0s       max=2.67ms   p(90)=0s     p(95)=0s
     http_req_duration..............: avg=1.22ms  min=74µs     med=738µs    max=113.56ms p(90)=2.51ms p(95)=3.68ms
       { expected_response:true }...: avg=1.22ms  min=74µs     med=738µs    max=113.56ms p(90)=2.51ms p(95)=3.68ms
     http_req_failed................: 0.00%   0 out of 1000000
     http_req_receiving.............: avg=70.99µs min=9µs      med=23µs     max=110.82ms p(90)=36µs   p(95)=68µs
     http_req_sending...............: avg=30.44µs min=4µs      med=11µs     max=73.81ms  p(90)=16µs   p(95)=22µs
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s       max=0s       p(90)=0s     p(95)=0s
     http_req_waiting...............: avg=1.11ms  min=51µs     med=686µs    max=111.44ms p(90)=2.38ms p(95)=3.44ms
     http_reqs......................: 1000000 32275.779755/s
     iteration_duration.............: avg=1.52ms  min=129.43µs med=919.75µs max=116.47ms p(90)=3.03ms p(95)=4.65ms
     iterations.....................: 1000000 32275.779755/s
     vus............................: 50      min=50                 max=50
     vus_max........................: 50      min=50                 max=50


running (0h00m31.0s), 00/50 VUs, 1000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h00m31.0s/1h0m0s  1000000/1000000 shared iters
```

### **10 Million Requests**
```bash
k6 run -u 50 -i 10000000 --duration 1h --tag testname=ten_million_request_test test.js
```

**Key Metrics**:
```
thehellmaker@thehellmakers-MacBook-Pro test %  k6 run -u 50 -i 10000000 --duration 1h --tag testname=ten_million_request_test test.js

         /\      Grafana   /‾‾/
    /\  /  \     |\  __   /  /
   /  \/    \    | |/ /  /   ‾‾\
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/

     execution: local
        script: test.js
        output: -

     scenarios: (100.00%) 1 scenario, 50 max VUs, 1h0m30s max duration (incl. graceful stop):
              * default: 10000000 iterations shared among 50 VUs (maxDuration: 1h0m0s, gracefulStop: 30s)


     ✓ Status is 200
     ✓ Correct JSON response

     checks.........................: 100.00%  20000000 out of 20000000
     data_received..................: 1.3 GB   3.1 MB/s
     data_sent......................: 1.6 GB   3.8 MB/s
     http_req_blocked...............: avg=8.41µs  min=1µs      med=5µs    max=124.58ms p(90)=6µs    p(95)=7µs
     http_req_connecting............: avg=29ns    min=0s       med=0s     max=18.84ms  p(90)=0s     p(95)=0s
     http_req_duration..............: avg=1.74ms  min=65µs     med=1.08ms max=161.6ms  p(90)=3.58ms p(95)=5.27ms
       { expected_response:true }...: avg=1.74ms  min=65µs     med=1.08ms max=161.6ms  p(90)=3.58ms p(95)=5.27ms
     http_req_failed................: 0.00%    0 out of 10000000
     http_req_receiving.............: avg=76.71µs min=8µs      med=33µs   max=157.11ms p(90)=40µs   p(95)=58µs
     http_req_sending...............: avg=31.98µs min=4µs      med=15µs   max=158.07ms p(90)=18µs   p(95)=21µs
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s     p(95)=0s
     http_req_waiting...............: avg=1.63ms  min=48µs     med=1.02ms max=153.94ms p(90)=3.43ms p(95)=5ms
     http_reqs......................: 10000000 23400.293679/s
     iteration_duration.............: avg=2.1ms   min=129.96µs med=1.3ms  max=161.75ms p(90)=4.17ms p(95)=6.27ms
     iterations.....................: 10000000 23400.293679/s
     vus............................: 50       min=50                   max=50
     vus_max........................: 50       min=50                   max=50


running (0h07m07.3s), 00/50 VUs, 10000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h07m07.3s/1h0m0s  10000000/10000000 shared iters
```

---

## **Project Structure**
```
.
├── Cargo.toml            # Rust dependencies and config
├── src/
│   ├── main.rs           # Server implementation
│   └── handlers.rs       # Request handlers
└── .gitignore            # Ignores target/ and build files
```

---

## **License**
This project is licensed under the [Apache License 2.0](LICENSE).
```