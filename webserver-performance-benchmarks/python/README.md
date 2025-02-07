# **FastAPI WebServer Performance Monitoring**

A minimal Python webserver built with **FastAPI** behind **Uvicorn** for analyzing server performance. Exposes a simple API endpoint `/test`.

---

## **Getting Started**

### **Prerequisites**
- [Python](https://www.python.org/downloads/) (3.8 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) package manager

### **Installation**
1. Create virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   pip install -r requirements.txt
   ```

2. Start the server with 24 workers:
   ```bash
   uvicorn main:app --port 8080 --workers 24
   ```
3. Server will be available at:
   ```txt
   http://localhost:8080
   ```

---

## **Endpoints**

### **CURL POST /test**
Process JSON payload, log the `graphName`, and return the same JSON.
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
- **24 Uvicorn workers**

### **1 Million Requests - 1 Worker**
```bash
k6 run -u 50 -i 1000000 --duration 1h --tag testname=million_request_test test.js
```

**Key Metrics**:
```
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
     data_received..................: 150 MB  197 kB/s
     data_sent......................: 162 MB  212 kB/s
     http_req_blocked...............: avg=3.13µs  min=1µs     med=3µs     max=19.3ms   p(90)=4µs     p(95)=5µs
     http_req_connecting............: avg=71ns    min=0s      med=0s      max=1.71ms   p(90)=0s      p(95)=0s
     http_req_duration..............: avg=38.02ms min=20.81ms med=36.08ms max=259.65ms p(90)=43.92ms p(95)=50.99ms
       { expected_response:true }...: avg=38.02ms min=20.81ms med=36.08ms max=259.65ms p(90)=43.92ms p(95)=50.99ms
     http_req_failed................: 0.00%   0 out of 1000000
     http_req_receiving.............: avg=45.21µs min=18µs    med=36µs    max=74.1ms   p(90)=69µs    p(95)=91µs
     http_req_sending...............: avg=14.77µs min=5µs     med=13µs    max=30.85ms  p(90)=19µs    p(95)=23µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=37.96ms min=20.72ms med=36.02ms max=259.56ms p(90)=43.85ms p(95)=50.91ms
     http_reqs......................: 1000000 1310.914244/s
     iteration_duration.............: avg=38.12ms min=20.95ms med=36.18ms max=259.81ms p(90)=44.03ms p(95)=51.14ms
     iterations.....................: 1000000 1310.914244/s
     vus............................: 50      min=50                 max=50
     vus_max........................: 50      min=50                 max=50


running (0h12m42.8s), 00/50 VUs, 1000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h12m42.8s/1h0m0s  1000000/1000000 shared iters
```

### **1 Million Requests - 24 Worker for a 12 Core machine**
```bash
k6 run -u 50 -i 1000000 --duration 1h --tag testname=million_request_test test.js
```

**Key Metrics**:
```
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
     data_received..................: 150 MB  561 kB/s
     data_sent......................: 162 MB  606 kB/s
     http_req_blocked...............: avg=5.91µs   min=1µs    med=5µs     max=4.23ms   p(90)=7µs     p(95)=8µs
     http_req_connecting............: avg=72ns     min=0s     med=0s      max=1.91ms   p(90)=0s      p(95)=0s
     http_req_duration..............: avg=13.14ms  min=1.2ms  med=9.94ms  max=198.29ms p(90)=24.87ms p(95)=34.95ms
       { expected_response:true }...: avg=13.14ms  min=1.2ms  med=9.94ms  max=198.29ms p(90)=24.87ms p(95)=34.95ms
     http_req_failed................: 0.00%   0 out of 1000000
     http_req_receiving.............: avg=221.74µs min=17µs   med=73µs    max=125.3ms  p(90)=325µs   p(95)=602µs
     http_req_sending...............: avg=22.28µs  min=6µs    med=19µs    max=13.98ms  p(90)=31µs    p(95)=35µs
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=12.89ms  min=1.16ms med=9.75ms  max=197.45ms p(90)=24.41ms p(95)=34.36ms
     http_reqs......................: 1000000 3742.711911/s
     iteration_duration.............: avg=13.33ms  min=1.3ms  med=10.13ms max=198.59ms p(90)=25.07ms p(95)=35.15ms
     iterations.....................: 1000000 3742.711911/s
     vus............................: 50      min=50                 max=50
     vus_max........................: 50      min=50                 max=50


running (0h04m27.2s), 00/50 VUs, 1000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h04m27.2s/1h0m0s  1000000/1000000 shared iters
```

### **10 Million Requests - 24 Worker for a 12 Core machine**
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
     data_received..................: 1.5 GB   514 kB/s
     data_sent......................: 1.6 GB   555 kB/s
     http_req_blocked...............: avg=6.19µs   min=2µs    med=6µs    max=4.7ms    p(90)=7µs     p(95)=9µs
     http_req_connecting............: avg=9ns      min=0s     med=0s     max=3.1ms    p(90)=0s      p(95)=0s
     http_req_duration..............: avg=14.35ms  min=1.45ms med=7.73ms max=421.08ms p(90)=28.14ms p(95)=51.03ms
       { expected_response:true }...: avg=14.35ms  min=1.45ms med=7.73ms max=421.08ms p(90)=28.14ms p(95)=51.03ms
     http_req_failed................: 0.00%    0 out of 10000000
     http_req_receiving.............: avg=237.61µs min=23µs   med=74µs   max=359.3ms  p(90)=248µs   p(95)=401µs
     http_req_sending...............: avg=23.61µs  min=8µs    med=20µs   max=165.09ms p(90)=31µs    p(95)=35µs
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s     max=0s       p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=14.09ms  min=1.39ms med=7.57ms max=278.57ms p(90)=27.41ms p(95)=49.94ms
     http_reqs......................: 10000000 3428.600147/s
     iteration_duration.............: avg=14.56ms  min=1.58ms med=7.95ms max=421.26ms p(90)=28.35ms p(95)=51.24ms
     iterations.....................: 10000000 3428.600147/s
     vus............................: 50       min=50                   max=50
     vus_max........................: 50       min=50                   max=50


running (0h48m36.6s), 00/50 VUs, 10000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h48m36.6s/1h0m0s  10000000/10000000 shared iters
```

---

## **Project Structure**
```
.
├── main.py               # FastAPI application setup
├── requirements.txt      # Dependencies (FastAPI, uvicorn)
```

---

## **Optimization Notes**
- 24 workers leverage CPU cores efficiently (ideal for 12-core CPUs with hyper-threading)
- Worker count should match available CPU cores for optimal performance
- Async I/O handling in FastAPI complements worker parallelism

---

## **License**
This project is licensed under the [Apache License 2.0](LICENSE).

---

*Adjust worker count based on your CPU cores. Results may vary depending on hardware and network conditions.*
```