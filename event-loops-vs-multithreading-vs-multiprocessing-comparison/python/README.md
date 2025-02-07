# Performance Comparison: Event Loops vs Multithreading vs Multiprocessing

This document compares different concurrency approaches in Python for processing URLs.

## Test Results Summary

| Approach | 100K URLs (seconds) | 1M URLs (seconds) |
|----------|-------------------|-------------------|
| AsyncIO (No Batching) | 29.84 | 164.81 |
| AsyncIO (with Batching) | 24.62 | 137.78 |
| Multiprocessing + AsyncIO | 11.97 | 83.54 |
| Multithreading (Pool) | 562.45 | 5410.76 |
| Multithreading (Basic) | 530.99 | 5280.92 |
| Serial Implementation | 1106.08 | 11243.92 |

## Detailed Results

### 1. AsyncIO (Single-Threaded Event Loop)
```bash
python asyncio_no_batch_test.py
```

#### Results:
##### 100000 urls
- Task creation time: 0.51 seconds
- Task execution time: 29.26 seconds
- Total execution time: 29.77 seconds
- Total script execution time: 29.84 seconds

##### 1 million urls
- Task creation time: 5.62 seconds
- Task execution time: 159.19 seconds
- Total execution time: 164.81 seconds


### 2. AsyncIO with Batching
```bash
python asyncio_batch_test.py
```

#### Results:
##### 100000 urls
- Average batch processing time: ~2.46 seconds
- Total execution time: 24.61 seconds
- Total script execution time: 24.62 seconds
- Batch size: 10,000 URLs

##### 1 million urls
- Average batch processing time: ~1.37 seconds
- Total execution time: 137.78 seconds
- Batch size: 10,000 URLs

### 3. Multiprocessing + AsyncIO
```bash
python multiprocessasynciotest.py
```

#### Results:
##### 100000 urls
- Total execution time: 11.97 seconds

##### 1 million urls
- Total execution time: 83.54 seconds

### 4. Multithreading Approaches

#### Pool Implementation
```bash
python multithreadingpooltest.py
```

#### Results:
##### 100000 urls
- Total execution time: 562.45 seconds

##### 1 million urls
- Total execution time: 5410.76 seconds

#### Basic Implementation
```bash
python multithreadingtest.py
```

#### Results:
##### 100000 urls
- Total execution time: 530.99 seconds

##### 1 million urls
- Total execution time: 5280.92 seconds

### 5. Serial Implementation
```bash
python serial.py
```

#### Results:
##### 100000 urls
- Total execution time: 1106.08 seconds

##### 1 million urls
- Total execution time: 11243.92 seconds

## Test Environment

The tests were performed against a local Go test server from the [webserver-performance-benchmarks](../webserver-performance-benchmarks/go) project. The server implements a simple JSON parsing and response endpoint, making it ideal for testing different concurrency approaches.

The test server code is written in Go and provides consistent response times by parsing incoming JSON requests and returning JSON responses, ensuring reliable benchmarking conditions across all concurrency implementations.

The server was run on a MacBook Pro 2018 on x86 intel processor with 16GB of RAM. And the clients were also run on the same machine and not on different machines. This was done due to ease of benchmarking. Though absolute numbers might not be super accurate, the relative performance of the different concurrency approaches should give a good indication of the performance of each approach.

## Key Findings

1. **Most Efficient**: Multiprocessing + AsyncIO combination provides the best performance, completing the task in 83.54 seconds.
2. **Batching Impact**: AsyncIO with batching (137.78s) shows significant improvement over non-batched AsyncIO (164.81s).
3. **Least Efficient**: Both multithreading approaches performed significantly slower, taking over 5000 seconds each.

This comparison demonstrates the significant performance advantages of using AsyncIO and multiprocessing over traditional multithreading for I/O-bound tasks in Python.

# Python Asyncio URL Fetcher Example

This example demonstrates how to use Python's asyncio and aiohttp to perform concurrent HTTP requests efficiently using event loops.

## Prerequisites

1. Python 3.7 or higher
2. Required packages:
   ```bash
   pip install aiohttp
   ```

## Running the Example

1. First, make sure you have a test server running on `http://localhost:8080/ping`. You can use any of these options:
   - Python's built-in HTTP server
   - Node.js express server
   - Any other HTTP server that can handle concurrent requests

2. Run the asyncio test:
   ```bash
   python asynciotest.py
   ```

## How It Works

The code demonstrates several key concepts:

1. **Concurrency Control**: 
   - Uses `MAX_CONCURRENCY` to limit simultaneous connections
   - Processes URLs in batches to manage memory usage

2. **Session Management**:
   - Uses `aiohttp.ClientSession` for efficient connection reuse
   - Properly manages async resources with context managers

3. **Error Handling**:
   - Gracefully handles failed requests
   - Provides progress feedback during execution

## Configuration

You can modify these parameters in the code:

- `MAX_CONCURRENCY`: Maximum number of concurrent connections (default: 1000)
- `urls`: List of URLs to test (default: 100,000 requests to localhost)

## Performance Notes

- The asyncio implementation is ideal for I/O-bound tasks like HTTP requests
- It uses a single thread but can handle many concurrent connections
- Memory usage is controlled through batch processing
- Performance will vary based on:
  - Network conditions
  - Server capacity
  - System resources
  - Number of concurrent connections

## Comparison with Other Approaches

This implementation offers several advantages:
- Lower memory footprint compared to threading
- Better resource utilization than multiprocessing for I/O-bound tasks
- Explicit concurrency control
- Non-blocking I/O operations

## Troubleshooting

1. If you see connection errors:
   - Verify the test server is running
   - Check if the port is correct
   - Reduce `MAX_CONCURRENCY` if server is overwhelmed

2. If you experience memory issues:
   - Reduce the batch size
   - Decrease the number of concurrent connections
   - Monitor system resources during execution
