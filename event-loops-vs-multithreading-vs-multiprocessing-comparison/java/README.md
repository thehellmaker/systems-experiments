# Performance Comparison: Virtual Threads vs Platform Threads vs Reactive Programming

This document compares different concurrency approaches in Java for processing URLs.

## Test Results Summary

| Approach | 100K URLs (seconds) | 1M URLs (seconds) |
|----------|-------------------|-------------------|
| Vert.x Event Loop | 5.60 | 38.8 |
| Virtual Threads (Java 21) | 7.46 | 56.2 |
| Platform Threads (Thread Pool) | 7.04 | 74.2 |
| Single Threaded | 16.48 | 163.90 |

## Detailed Results

### 1. Vert.x Event Loop
```bash
mvn clean package exec:java -Dexec.mainClass="com.thehellmaker.VertxClient"
```

#### Results:
##### 100000 urls
- Total execution time: 5.60 seconds

##### 1 million urls
- Total execution time: 38.8 seconds

### 2. Virtual Threads (Java 21)
```bash
mvn clean package exec:java -Dexec.mainClass="com.thehellmaker.VirtualThreadClient"
```

#### Results:
##### 100000 urls
- Total execution time: 7.46 seconds

##### 1 million urls
- Total execution time: 56.2 seconds

### 3. Platform Threads (Thread Pool)
```bash
mvn clean package exec:java -Dexec.mainClass="com.thehellmaker.MultithreadingClient"
```

#### Results:
##### 100000 urls
- Total execution time: 7.04 seconds

##### 1 million urls
- Total execution time: 74.2 seconds

### 4. Single Threaded
```bash
mvn clean package exec:java -Dexec.mainClass="com.thehellmaker.SerialClient"
```

#### Results:
##### 100000 urls
- Total execution time: 16.48 seconds

##### 1 million urls
- Total execution time: 163.90 seconds

## Test Environment

The tests were performed against a local Go test server from the [webserver-performance-benchmarks](../webserver-performance-benchmarks/go) project. The server implements a simple JSON parsing and response endpoint, making it ideal for testing different concurrency approaches.

The test server code is written in Go and provides consistent response times by parsing incoming JSON requests and returning JSON responses, ensuring reliable benchmarking conditions across all concurrency implementations.

The server was run on a MacBook Pro 2018 on x86 intel processor with 16GB of RAM. And the clients were also run on the same machine and not on different machines. This was done due to ease of benchmarking. Though absolute numbers might not be super accurate, the relative performance of the different concurrency approaches should give a good indication of the performance of each approach.

## Key Findings

1. **Most Efficient**: Vert.x Event Loop demonstrates the best performance, completing 1 million URLs in 38.8 seconds.
2. **Strong Runner-up**: Virtual Threads (Java 21) shows excellent performance at 56.2 seconds.
3. **Traditional Approach**: Platform threads performed notably slower at 74.2 seconds.
4. **Baseline Comparison**: Single-threaded execution was significantly slower at 163.90 seconds, highlighting the benefits of concurrent approaches.

This comparison demonstrates that event-loop based programming provides the best performance for I/O-bound tasks in Java, followed closely by Virtual Threads. Both approaches significantly outperform traditional platform threads for high-concurrency I/O operations.

## Prerequisites

Java 21 or higher (for Virtual Threads)

## Running the Example

1. Ensure you have a test server running on `http://localhost:8080/ping`
