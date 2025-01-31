# Webserver Performance Benchmarks (Multi Language & Framework)

This repository contains simple web servers written in **Go (Gin)**, **Rust**, **Node.js (Express)**, **TypeScript (Express)**, and **Python (FastAPI)**. Each server performs the same task:

1. Accepts a JSON request with the format 
```json
{
    "graphName": "xyz"
}
```
2. Parses the JSON and prints the `graphName`.
3. Returns the same JSON as the response.

All servers are designed to be lightweight and easy to test. Each server runs on **port 8080**, so you can test them one at a time.

---

## **How to Run**

### **1. Clone the Repository**
```bash
git clone https://github.com/thehellmaker/webserver-performance-benchmarks.git
cd webserver-performance-benchmarks
```

### **2. Run the Servers**
Each server can be started independently. Navigate to the respective directory and follow the README instructions.

---

## **Testing with k6**

### **1. Install k6**
Follow the [k6 installation guide](https://k6.io/docs/getting-started/installation/) for your platform.

### **2. Go to the test folder**
```bash
cd test
```

### **3. Run the k6 Script**
A k6 script (`test.js`) is provided to test the server. Ensure the server is running on **port 8080** before executing the script by going to the respective language folder and running it.

## 1M requests
```bash
 k6 run -u 50 -i 1000000 --duration 1h --tag testname=million_request_test test.js
```

## 10M requests
```bash
 k6 run -u 50 -i 10000000 --duration 1h --tag testname=10_million_request_test test.js
```

The results of these benchmarks have been updated in the respective folders of different languages

---

## Performance Numbers

### 1M Requests (Respective Language folders have full details)

| Language                          | min      | p50      | p90      | p95      | max       | Total Runtime |
|-----------------------------------|----------|----------|----------|----------|-----------|---------------|
| **Rust (Actix)**                  | 74    us | 738   us | 2.51  ms | 3.68  ms | 113.56 ms |        31 s   |
| **Go (Gin)**                      | 108   us | 2.64  ms | 7.05  ms | 8.88  ms | 114.26 ms |    1 m 11 s   |
| **Node.js (Express/JS)**          | 714   us | 11.62 ms | 14.5  ms | 15.58 ms | 429.31 ms |    4 m 02 s   |
| **Node.js (Express/TS)**          | 1.87  ms | 11.22 ms | 14.34 ms | 15.78 ms | 467.67 ms |    3 m 57 s   |
| **Python (FastAPI)**  (24 Worker) | 1.2   ms | 9.94  ms | 24.87 ms | 34.95 ms | 198.29 ms |    4 m 27 s   |     
| **Python (FastAPI)**  (1 Worker)  | 20.81 ms | 36.08 ms | 43.92 ms | 50.99 ms | 259.65 ms |   12 m 42 s   |    


### 10M Requests (Respective Language folders have full details)

| Language                          | min      | p50      | p90      | p95      | max       | Total Runtime |
|-----------------------------------|----------|----------|----------|----------|-----------|---------------|
| **Rust (Actix)**                  | 65    us | 1.08  ms | 3.58  ms | 5.27  ms | 161.6  ms |    7 m 07 s   |
| **Go (Gin)**                      | 99    us | 2.69  ms | 7.13  ms | 8.93  ms | 144.52 ms |   11 m 50 s   |
| **Node.js (Express/JS)**          | 445   us | 11.46 ms | 13.61 ms | 14.77 ms | 429.83 ms |   40 m 25 s   |
| **Node.js (Express/TS)**          | 547   us | 12.77 ms | 16.66 ms | 19.06 ms | 548.57 ms |   46 m 49 s   |
| **Python (FastAPI)**  (24 Worker) | 1.45  ms | 7.73  ms | 28/14 ms | 51.03 ms | 421.08 ms |   48 m 36 s   |   


## **License**

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request for any improvements or fixes.

---

## **Acknowledgments**

- Thanks to the developers of Go, Rust, Node.js, TypeScript, and FastAPI for their amazing frameworks.
- Special thanks to the k6 team for providing a powerful load-testing tool.

---

Enjoy testing and exploring the multi-language web servers performance benchmarks! 🚀