# **Node.js Express WebServer Performance Monitoring**

A minimal Node.js webserver built with the **Express** framework for analyzing server performance. Exposes a simple API endpoint `/test`.

---

## **Getting Started**

### **Prerequisites**
- [Node.js](https://nodejs.org/) (v18.x or higher)
- [npm](https://www.npmjs.com/) (v9.x or higher)

### **Installation**
1. Install dependencies:
   ```bash
   npm install
   tsc
   ```

2. Run the webserver:
   ```bash
   node dist/app.js
   ```

3. The server will start on port `8080` with the following log:
   ```txt
   Example app listening on port 8080
   ```

---

## **Endpoints**

### **CURL POST /test**
Parses a JSON payload, logs the `graphName` field, and echoes the JSON back as the response.
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

**Results**:
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
     data_received..................: 260 MB  1.1 MB/s
     data_sent......................: 162 MB  682 kB/s
     http_req_blocked...............: avg=2.64µs  min=1µs    med=2µs     max=3.3ms    p(90)=3µs     p(95)=4µs
     http_req_connecting............: avg=92ns    min=0s     med=0s      max=2.21ms   p(90)=0s      p(95)=0s
     http_req_duration..............: avg=11.77ms min=1.87ms med=11.22ms max=467.67ms p(90)=14.34ms p(95)=15.78ms
       { expected_response:true }...: avg=11.77ms min=1.87ms med=11.22ms max=467.67ms p(90)=14.34ms p(95)=15.78ms
     http_req_failed................: 0.00%   0 out of 1000000
     http_req_receiving.............: avg=27µs    min=14µs   med=24µs    max=8.83ms   p(90)=36µs    p(95)=43µs
     http_req_sending...............: avg=12.78µs min=4µs    med=12µs    max=6.34ms   p(90)=16µs    p(95)=18µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=11.73ms min=1.83ms med=11.18ms max=467.6ms  p(90)=14.29ms p(95)=15.73ms
     http_reqs......................: 1000000 4212.476914/s
     iteration_duration.............: avg=11.85ms min=2ms    med=11.31ms max=470.52ms p(90)=14.44ms p(95)=15.88ms
     iterations.....................: 1000000 4212.476914/s
     vus............................: 50      min=50                 max=50
     vus_max........................: 50      min=50                 max=50


running (0h03m57.4s), 00/50 VUs, 1000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h03m57.4s/1h0m0s  1000000/1000000 shared iters
```

### **10 Million Requests**
```bash
k6 run -u 50 -i 10000000 --duration 1h --tag testname=ten_million_request_test test.js
```

**Results**:
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
     data_received..................: 2.6 GB   926 kB/s
     data_sent......................: 1.6 GB   577 kB/s
     http_req_blocked...............: avg=2.81µs  min=1µs      med=2µs     max=20.49ms  p(90)=4µs     p(95)=4µs
     http_req_connecting............: avg=7ns     min=0s       med=0s      max=1.83ms   p(90)=0s      p(95)=0s
     http_req_duration..............: avg=13.93ms min=541µs    med=12.77ms max=548.57ms p(90)=16.66ms p(95)=19.06ms
       { expected_response:true }...: avg=13.93ms min=541µs    med=12.77ms max=548.57ms p(90)=16.66ms p(95)=19.06ms
     http_req_failed................: 0.00%    0 out of 10000000
     http_req_receiving.............: avg=32.87µs min=14µs     med=26µs    max=244.09ms p(90)=42µs    p(95)=55µs
     http_req_sending...............: avg=14.87µs min=4µs      med=13µs    max=244.45ms p(90)=18µs    p(95)=23µs
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=13.89ms min=473µs    med=12.72ms max=548.42ms p(90)=16.6ms  p(95)=18.99ms
     http_reqs......................: 10000000 3560.005447/s
     iteration_duration.............: avg=14.03ms min=672.71µs med=12.86ms max=548.84ms p(90)=16.77ms p(95)=19.18ms
     iterations.....................: 10000000 3560.005447/s
     vus............................: 50       min=50                   max=50
     vus_max........................: 50       min=50                   max=50


running (0h46m49.0s), 00/50 VUs, 10000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h46m48.9s/1h0m0s  10000000/10000000 shared iters
```

---

## **Project Structure**
```
.
├── server.js           # Core server configuration
├── package.json        # Dependencies and scripts
└── .gitignore          # Excludes node_modules and logs
```

---

## **License**
This project is licensed under the [Apache License 2.0](LICENSE).