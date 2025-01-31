# **WebServer Performance Monitoring**

A minimal Go webserver built with the **Gin** framework for analyzing go's performance. Exposes a simple API called /test.

---

## **Getting Started**

### **Prerequisites**
- [Go](https://golang.org/doc/install) (version 1.20 or higher)

### **Installation**
1. Install dependencies:
   ```bash
   go mod tidy
   ```

2. Run the webserver:
   ```bash
   go run main.go
   ```
3. The server will be running on 8080 port and a log message as shown below should be printed on the console
    ```txt
    [GIN-debug] Listening and serving HTTP on localhost:8080
    ```
---

## **Endpoints**

### **CURL POST /test**
This parses a json with the below requests structure, logs the graphName from the json and returns the same JSON.
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"graphName":"xyz"}' \
  http://localhost:8080/test
```

Response example:
```json
{
    "GraphName":"xyz"
}
```

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
     data_received..................: 148 MB  2.1 MB/s
     data_sent......................: 162 MB  2.3 MB/s
     http_req_blocked...............: avg=6.31µs  min=1µs      med=4µs    max=16.15ms  p(90)=6µs    p(95)=6µs
     http_req_connecting............: avg=71ns    min=0s       med=0s     max=2.14ms   p(90)=0s     p(95)=0s
     http_req_duration..............: avg=3.32ms  min=108µs    med=2.64ms max=114.26ms p(90)=7.05ms p(95)=8.88ms
       { expected_response:true }...: avg=3.32ms  min=108µs    med=2.64ms max=114.26ms p(90)=7.05ms p(95)=8.88ms
     http_req_failed................: 0.00%   0 out of 1000000
     http_req_receiving.............: avg=78.5µs  min=10µs     med=33µs   max=34.86ms  p(90)=68µs   p(95)=115µs
     http_req_sending...............: avg=28.82µs min=4µs      med=14µs   max=62.36ms  p(90)=21µs   p(95)=38µs
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s     p(95)=0s
     http_req_waiting...............: avg=3.21ms  min=79µs     med=2.56ms max=114.21ms p(90)=6.89ms p(95)=8.64ms
     http_reqs......................: 1000000 14019.094736/s
     iteration_duration.............: avg=3.54ms  min=201.66µs med=2.85ms max=114.49ms p(90)=7.31ms p(95)=9.17ms
     iterations.....................: 1000000 14019.094736/s
     vus............................: 50      min=50                 max=50
     vus_max........................: 50      min=50                 max=50


running (0h01m11.3s), 00/50 VUs, 1000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h01m11.3s/1h0m0s  1000000/1000000 shared iters
```

### **10 Million Requests**
```bash
k6 run -u 50 -i 10000000 --duration 1h --tag testname=ten_million_request_test test.js
```

**Results**:
```
thehellmaker@thehellmakers-MacBook-Pro test %  k6 run -u 50 -i 10000000 --duration 1h --tag testname=million_request_test test.js

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
     data_received..................: 1.5 GB   2.1 MB/s
     data_sent......................: 1.6 GB   2.3 MB/s
     http_req_blocked...............: avg=5.28µs  min=1µs      med=4µs    max=47.62ms  p(90)=5µs    p(95)=6µs
     http_req_connecting............: avg=6ns     min=0s       med=0s     max=1.84ms   p(90)=0s     p(95)=0s
     http_req_duration..............: avg=3.34ms  min=99µs     med=2.69ms max=144.52ms p(90)=7.13ms p(95)=8.93ms
       { expected_response:true }...: avg=3.34ms  min=99µs     med=2.69ms max=144.52ms p(90)=7.13ms p(95)=8.93ms
     http_req_failed................: 0.00%    0 out of 10000000
     http_req_receiving.............: avg=50.61µs min=9µs      med=34µs   max=134.49ms p(90)=63µs   p(95)=86µs
     http_req_sending...............: avg=19.1µs  min=4µs      med=15µs   max=134.46ms p(90)=20µs   p(95)=32µs
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s     p(95)=0s
     http_req_waiting...............: avg=3.27ms  min=68µs     med=2.63ms max=126.83ms p(90)=7.05ms p(95)=8.84ms
     http_reqs......................: 10000000 14083.411472/s
     iteration_duration.............: avg=3.53ms  min=167.25µs med=2.87ms max=146.11ms p(90)=7.33ms p(95)=9.13ms
     iterations.....................: 10000000 14083.411472/s
     vus............................: 50       min=50                   max=50
     vus_max........................: 50       min=50                   max=50


running (0h11m50.1s), 00/50 VUs, 10000000 complete and 0 interrupted iterations
default ✓ [======================================] 50 VUs  0h11m50.1s/1h0m0s  10000000/10000000 shared iters
```

---

## **License**
This project is licensed under the [Apache License 2.0](LICENSE).

