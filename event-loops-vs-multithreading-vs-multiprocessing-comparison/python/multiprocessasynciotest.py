import asyncio
import json
import aiohttp
import time
import backoff
from multiprocessing import Process, Queue, cpu_count

# Generate 100 URLs
urls = ["http://localhost:8080/ping"] * 1000000

# Split URLs into chunks for each process
def chunk_list(lst, num_chunks):
    chunk_size = len(lst) // num_chunks
    return [lst[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]


@backoff.on_exception(
    backoff.expo,
    Exception,
    max_tries=10,  # 50 retries, TODO - Need to reduce this
    jitter=backoff.full_jitter,
)
# Async function to fetch URLs
async def fetch(url, session):
    async with session.get(url) as response:
        response = await response.text()
        return json.loads(response)

# Async function to process a chunk of URLs
async def process_chunk(url_chunk, result_queue):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(url, session)) for url in url_chunk]
        for task in tasks:
            await task
    # result_queue.put(results)

# Function for each process to create an event loop and run tasks
def worker(url_chunk, result_queue):
    asyncio.run(process_chunk(url_chunk, result_queue))

# Main function to manage multiprocessing
def main():
    num_processes = max(cpu_count(), 12)  # Use up to 4 processes
    url_chunks = chunk_list(urls, num_processes)
    result_queue = Queue()

    processes = [
        Process(target=worker, args=(chunk, result_queue))
        for chunk in url_chunks
    ]

    start_time = time.time()

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    results = []
    while not result_queue.empty():
        results.extend(result_queue.get())

    end_time = time.time()
    print(f"Multiprocessing with Asyncio Time: {end_time - start_time:.2f} seconds")
    print(f"Total responses received: {len(results)}")
            
if __name__ == "__main__":
    main()