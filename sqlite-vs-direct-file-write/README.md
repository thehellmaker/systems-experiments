# Performance Benchmark: SQLite vs. Direct File Writes  

This project benchmarks the performance of writing data **directly to a file** versus inserting data into **SQLite** under different conditions.  The [Blog](https://thehellmaker.vercel.app/blog/are-sqlite-faster-than-direct-file-writes/) explains this code repo in detail.

## 📌 Experiments & Commands  

### **Experiment 1: SQLite vs. Direct File Writes**  
#### Run:  
```sh
mkdir -p bin && cargo run --bin expt1
```  
#### Output (Example):  
```
Time Taken For SQLite = 1941 ms  
Time Taken For Direct File Writes = 6197 ms  
```  

### **Experiment 2: Bulk Writes & Sleep Delay Impact**  
#### Run:  
```sh
mkdir -p bin && cargo run --bin expt2
```  
#### Output (Example):  
```
100k Write Time Taken = 1466 ms  
... (Repeats with sleep intervals)  
100k Write Time Taken = 1593 ms  
```  

### **Experiment 3: Direct File Write Performance**  
#### Run:  
```sh
mkdir -p bin && cargo run --bin expt3
```  
#### Output (Example):  
```
Time Taken For Direct File Writes = 408 ms  
```  

## 📂 Project Structure  
```
/bin       # Compiled binaries  
/src/bin/  # Individual Rust experiments  
README.md  # Documentation  
Cargo.toml # Rust project configuration  
```  

## 📌 Notes  
- Ensure Rust and Cargo are installed before running the experiments.  
- Results may vary based on hardware and system configurations.  