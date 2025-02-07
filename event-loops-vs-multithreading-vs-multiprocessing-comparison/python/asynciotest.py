import asyncio
import aiohttp
import multiprocessing
from itertools import islice

# Number of parallel processes (depends on CPU cores)
NUM_PROCESSES = multiprocessing.cpu_count()  # Use all available cores
MAX_CONCURRENCY = 1000  # Max concurrent connections per process

# Generate 1M test URLs
urls = ["http://localhost:8080/ping"] * 100000   # Replace with real URLs

async def fetch(url, session):
    """Fetch a URL asynchronously with aiohttp."""
    try:
        async with session.get(url) as response:
            return await response.text()  # Process response if needed
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def main():    
    # Submit urls to an asyncio
    asyncio.run(main_async())



async def fetch_all(urls, session):
    """Fetch all URLs asynchronously with aiohttp."""
    tasks = []
    for url in urls:
        tasks.append(fetch(url, session))

    results = await asyncio.gather(*tasks)
    return results

            

async def main_async():
    session = aiohttp.ClientSession()
    for i in range(NUM_PROCESSES):
        asyncio.create_task(fetch_all(islice(urls, MAX_CONCURRENCY), session))
        
    await session.close()

# Main function: Press space to process them
def main():    
    # Test the function with 1M test URLs
    results = fetch_all(urls)
    for result in results:
        print(result)
       

    print("Processing complete!")

if __name__ == "__main__":
    main()