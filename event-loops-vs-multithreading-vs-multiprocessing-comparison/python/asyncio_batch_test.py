import asyncio
import aiohttp
import time
from config import NUM_URLS, TEST_URL

MAX_CONCURRENCY = 10000  # Max concurrent connections per batch

async def fetch(url, session):
    """Fetch a URL asynchronously with aiohttp."""
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def fetch_batch(urls_batch, session):
    """Fetch a batch of URLs with controlled concurrency."""
    tasks = []
    for url in urls_batch:
        tasks.append(fetch(url, session))
    return await asyncio.gather(*tasks)

async def main_async():
    """Main async function to process URLs in batches."""
    start_time = time.time()
    total_processed = 0
    
    # Configure client session with connection limit
    async with aiohttp.ClientSession() as session:
        batch_size = MAX_CONCURRENCY
        results = []
        urls = [TEST_URL] * NUM_URLS
        
        for i in range(0, len(urls), batch_size):
            batch_start = time.time()
            batch = urls[i:i + batch_size]
            batch_results = await fetch_batch(batch, session)
            results.extend(batch_results)
            total_processed += len(batch_results)
            
            batch_time = time.time() - batch_start
            total_time = time.time() - start_time
            print(f"Batch {i//batch_size + 1}/{len(urls)//batch_size + 1} "
                  f"completed in {batch_time:.2f} seconds")
            print(f"Total time so far: {total_time:.2f} seconds, "
                  f"Processed {total_processed} URLs")
        
        final_time = time.time() - start_time
        print(f"\nFinal execution time: {final_time:.2f} seconds")
        return results

def main():
    """Entry point of the program."""
    start_time = time.time()
    results = asyncio.run(main_async())
    
    total_time = time.time() - start_time
    print(f"Total URLs processed: {len(results)}")
    print(f"Total script execution time: {total_time:.2f} seconds")
    print("Processing complete!")

if __name__ == "__main__":
    main() 