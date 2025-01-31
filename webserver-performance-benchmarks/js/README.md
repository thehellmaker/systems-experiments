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
   ```

2. Run the webserver:
   ```bash
   node app.js
   ```

3. The server will start on port `8080` with the following log:
   ```txt
   Server running on http://localhost:8080
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
thehellmaker@thehellmakers-MacBook-Pro test %  k6 run -u 50 -i 1000000 --duration 1h --tag testname=million_request_test test.js

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
     data_sent......................: 162 MB  669 kB/s
     http_req_blocked...............: avg=2.45µs  min=1µs      med=2µs     max=2.75ms   p(90)=3µs     p(95)=4µs
     http_req_connecting............: avg=65ns    min=0s       med=0s      max=1.74ms   p(90)=0s      p(95)=0s
     http_req_duration..............: avg=12.01ms min=714µs    med=11.62ms max=429.31ms p(90)=14.5ms  p(95)=15.58ms
       { expected_response:true }...: avg=12.01ms min=714µs    med=11.62ms max=429.31ms p(90)=14.5ms  p(95)=15.58ms
     http_req_failed................: 0.00%   0 out of 1000000
     http_req_receiving.............: avg=25.58µs min=13µs     med=23µs    max=13.58ms  p(90)=34µs    p(95)=42µs
     http_req_sending...............: avg=12.28µs min=4µs      med=11µs    max=11.11ms  p(90)=15µs    p(95)=17µs
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=11.97ms min=676µs    med=11.58ms max=429.15ms p(90)=14.46ms p(95)=15.54ms
     http_reqs......................: 1000000 4129.390418/s
     iteration_duration.............: avg=12.09ms min=792.78µs med=11.7ms  max=430.62ms p(90)=14.59ms p(95)=15.67ms
     iterations.....................: 1000000 4129.390418/s
     vus............................: 50      min=50                 max=50
     vus_max........................: 50      min=50                 max=50


running (0h04m02.2s), 00/50 VUs, 1000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h04m02.2s/1h0m0s  1000000/1000000 shared iters
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
     data_received..................: 2.6 GB   1.1 MB/s
     data_sent......................: 1.6 GB   668 kB/s
     http_req_blocked...............: avg=2.52µs  min=1µs      med=2µs     max=63.72ms  p(90)=3µs     p(95)=3µs
     http_req_connecting............: avg=6ns     min=0s       med=0s      max=1.62ms   p(90)=0s      p(95)=0s
     http_req_duration..............: avg=12.03ms min=445µs    med=11.46ms max=429.83ms p(90)=13.61ms p(95)=14.77ms
       { expected_response:true }...: avg=12.03ms min=445µs    med=11.46ms max=429.83ms p(90)=13.61ms p(95)=14.77ms
     http_req_failed................: 0.00%    0 out of 10000000
     http_req_receiving.............: avg=28.25µs min=14µs     med=25µs    max=118.55ms p(90)=34µs    p(95)=39µs
     http_req_sending...............: avg=12.8µs  min=4µs      med=12µs    max=116.99ms p(90)=15µs    p(95)=17µs
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=11.99ms min=383µs    med=11.43ms max=429.73ms p(90)=13.57ms p(95)=14.73ms
     http_reqs......................: 10000000 4123.418759/s
     iteration_duration.............: avg=12.11ms min=677.57µs med=11.55ms max=430.98ms p(90)=13.7ms  p(95)=14.87ms
     iterations.....................: 10000000 4123.418759/s
     vus............................: 50       min=50                   max=50
     vus_max........................: 50       min=50                   max=50


running (0h40m25.2s), 00/50 VUs, 10000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h40m25.1s/1h0m0s  10000000/10000000 shared iters
```

---

## **Project Structure**
```
.
├── server.js           # Core server configuration
├── package.json        # Dependencies and scripts
├── test/               # Performance test scripts
│   └── test.js         # k6 test script
└── .gitignore          # Excludes node_modules and logs
```

---

## **Commands**
- **Start the server**: `node server.js`
- **Run performance tests**: 
  ```bash
  cd test && k6 run test.js
  ```

---

## **License**
This project is licensed under the [Apache License 2.0](LICENSE).