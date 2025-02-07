import asyncio
import aiohttp
import time
from config import NUM_URLS, TEST_URL

async def fetch(url, session):
    """Fetch a URL asynchronously with aiohttp."""
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def main_async(urls):
    """Main async function to process all URLs at once."""
    start_time = time.time()
    
    # Configure client session with no explicit connection limit
    async with aiohttp.ClientSession() as session:
        # Time task creation
        task_creation_start = time.time()
        tasks = [asyncio.create_task(fetch(url, session)) for url in urls]
        task_creation_time = time.time() - task_creation_start
        print(f"Task creation time: {task_creation_time:.2f} seconds")
        
        # Time task execution
        gather_start = time.time()
        results = []
        for completed_task in asyncio.as_completed(tasks):
            result = await completed_task
            results.append(result)
        gather_time = time.time() - gather_start
        print(f"Task execution time: {gather_time:.2f} seconds")
        
        total_time = time.time() - start_time
        print(f"\nTotal execution time: {total_time:.2f} seconds")
        return results

def main():
    """Entry point of the program."""
    start_time = time.time()
    urls = [TEST_URL] * NUM_URLS
    results = asyncio.run(main_async(urls))
    
    total_time = time.time() - start_time
    print(f"Total URLs processed: {len(results)}")
    print(f"Total script execution time: {total_time:.2f} seconds")
    print("Processing complete!")

if __name__ == "__main__":
    main() 