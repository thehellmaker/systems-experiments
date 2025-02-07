import httpx
import time
from config import NUM_URLS, TEST_URL

def fetch(url):
    """Fetch a URL synchronously with httpx."""
    try:
        response = httpx.get(url)
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    """Entry point of the program."""
    start_time = time.time()
    results = []
    urls = [TEST_URL] * NUM_URLS
    
    for i, url in enumerate(urls, 1):
        result = fetch(url)
        results.append(result)
        
        if i % 100 == 0:  # Print progress every 100 requests
            elapsed_time = time.time() - start_time
            print(f"Processed {i}/{NUM_URLS} URLs in {elapsed_time:.2f} seconds")
    
    total_time = time.time() - start_time
    print(f"\nTotal URLs processed: {len(results)}")
    print(f"Total script execution time: {total_time:.2f} seconds")
    print("Processing complete!")
    return results

if __name__ == "__main__":
    main() 