# Java vs Python Concurrency Performance Comparison

This repository compares different concurrency approaches in Java and Python for processing URLs.

## 100K URLs Latency Comparison (seconds)

| Approach | Java | Python |
|----------|------|--------|
| Event Loop Based | 5.60 (Vert.x) | 29.84 (AsyncIO) |
| Event Loop with Optimizations | - | 24.62 (AsyncIO + Batching) |
| Virtual/Platform Threads | 7.04 (Platform) / 7.46 (Virtual) | 530.99 (Basic) / 562.45 (Pool) |
| Multiprocessing | - | 11.97 (MP + AsyncIO) |
| Single Threaded | 16.48 | 1106.08 |

## 1M URLs Latency Comparison (seconds)

| Approach | Java | Python |
|----------|------|--------|
| Event Loop Based | 38.8 (Vert.x) | 164.81 (AsyncIO) |
| Event Loop with Optimizations | - | 137.78 (AsyncIO + Batching) |
| Virtual/Platform Threads | 74.2 (Platform) / 56.2 (Virtual) | 5280.92 (Basic) / 5410.76 (Pool) |
| Multiprocessing | - | 83.54 (MP + AsyncIO) |
| Single Threaded | 163.90 | 11243.92 |

## Key Observations

1. **Event Loop Performance**: Java's Vert.x consistently outperforms Python's AsyncIO by roughly 4-5x.

2. **Threading Comparison**: Java's threading implementations are significantly faster (70-100x) than Python's due to the Global Interpreter Lock (GIL).

3. **Best Approaches**:
   - Java: Vert.x Event Loop
   - Python: Multiprocessing + AsyncIO combination

For detailed implementation specifics and individual test results, please refer to:
- [Python Implementation Details](python/README.md)
- [Java Implementation Details](java/README.md)

## Test Environment

All tests were performed on a MacBook Pro 2018 (x86 intel processor, 16GB RAM) against a local Go test server. Both client and server were run on the same machine for consistent benchmarking conditions.
